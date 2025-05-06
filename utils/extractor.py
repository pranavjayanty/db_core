import os
import csv
import discord
import ssl
from dotenv import load_dotenv
from discord import TextChannel
from typing import List, Dict, Any, Optional

class DiscordExtractor:
    """
    A class that handles the extraction of data from Discord servers.
    
    This class provides methods to:
    - Export all messages from channels and their threads directly to CSV
    - Export channel information to CSV
    - Run the complete ETL pipeline
    
    The data is exported in a single format:
    - CSV file containing all messages with channel and thread information
    - CSV file containing channel information
    """
    
    def __init__(self):
        """
        Initialize the Discord extractor with required environment variables.
        
        Sets up:
        - Required directories for output files
        - SSL verification settings
        - Discord bot token and server ID from environment variables
        - Discord client intents (permissions)
        """
        # Ensure output directories exist
        os.makedirs("csv_files", exist_ok=True)
        
        # Disable SSL verification globally
        ssl._create_default_https_context = ssl._create_unverified_context
        
        # Loads Discord Token and Server ID environment variables
        load_dotenv()
        self.token = os.getenv("DARCY_KEY")
        self.guild_id = int(os.getenv("TEST_SERVER_ID"))
        
        # Set up Discord permissions (intents) to:
        # - Read message content
        # - Read guild information
        # - Read guild messages 
        self.intents = discord.Intents.default()
        self.intents.message_content = True
        self.intents.guilds = True
        self.intents.guild_messages = True

    def create_client(self) -> discord.Client:
        """
        Create a new Discord client with the configured intents.
        Returns:
            A new Discord client instance with the required permissions.
        """
        return discord.Client(intents=self.intents)

    async def export_channels(self) -> None:
        """
        Export channel information from Discord server to CSV.
        
        This method:
        1. Connects to Discord using the bot token
        2. Gets the guild (server) structure directly from Discord
        3. Extracts channel information (name and ID)
        4. Saves channel data to a CSV file
        
        The output CSV contains:
        - Channel name
        - Channel ID
        """
        client = self.create_client()

        @client.event
        async def on_ready():
            guild = client.get_guild(self.guild_id)
            if guild is None:
                print(f"❌ Guild ID {self.guild_id} not found.")
                await client.close()
                return

            channels = []
            
            # Process all text channels in the guild
            for channel in guild.text_channels:
                channels.append({
                    "channel_name": channel.name,
                    "channel_id": channel.id
                })
                print(f"✅ Extracted channel: {channel.name}")

            # Write channels to CSV
            csv_path = os.path.join("csv_files", "channels.csv")
            try:
                with open(csv_path, "w", encoding="utf-8", newline='') as f:
                    writer = csv.DictWriter(f, fieldnames=["channel_name", "channel_id"])
                    writer.writeheader()
                    writer.writerows(channels)
                
                print(f"✅ Wrote {csv_path} ({len(channels)} channels)")
            except Exception as e:
                print(f"❌ Error writing CSV file: {str(e)}")

            await client.close()

        await client.start(self.token)

    async def export_chat_history(self) -> None:
        """
        Export chat history from all channels and threads directly to CSV.
        
        This method:
        1. Connects to Discord using the bot token
        2. Gets the guild (server) structure directly from Discord
        3. For each channel:
           - Exports all messages from the main channel
           - Exports all messages from each thread in the channel
        4. Saves all messages to a CSV file
        
        The output CSV contains:
        - Channel information (ID, name)
        - Thread information (ID, name) if applicable
        - Message details (ID, author, content, timestamp)
        """
        # creates a Discord client with the configured permissions
        client = self.create_client()

        # event handler for when the client is ready
        @client.event
        async def on_ready():
            # gets the guild (server) structure directly from Discord   
            guild = client.get_guild(self.guild_id)
            if guild is None:
                print(f"❌ Guild ID {self.guild_id} not found.")
                await client.close()
                return

            all_messages = []
            total_messages = 0
            
            # Process all channels in the guild
            # - Loops through each text channel in the server
            # - Fetches all messages from each channel
            # - Stores message details  
            for channel in guild.text_channels:
                try:
                    print(f"🔄 Exporting {channel.name}...")
                    channel_messages = []
                    
                    # Export messages from the main channel
                    async for msg in channel.history(limit=None):
                        channel_messages.append({
                            "channel_name": channel.name,
                            "channel_id": channel.id,
                            "thread_name": None,
                            "thread_id": None,
                            "message_id": msg.id,
                            "author": msg.author.name,
                            "chat_text": msg.content,
                            "created_at": msg.created_at.isoformat()
                        })
                    
                    # Export messages from threads
                    # Get both active and archived threads
                    active_threads = channel.threads
                    archived_threads = []
                    async for thread in channel.archived_threads():
                        archived_threads.append(thread)
                    threads = active_threads + archived_threads
                    for thread in threads:
                        print(f"  🔄 Exporting thread: {thread.name}")
                        async for msg in thread.history(limit=None):
                            channel_messages.append({
                                "channel_name": channel.name,
                                "channel_id": channel.id,
                                "thread_name": thread.name,
                                "thread_id": thread.id,
                                "message_id": msg.id,
                                "author": msg.author.name,
                                "chat_text": msg.content,
                                "created_at": msg.created_at.isoformat()
                            })
                    
                    all_messages.extend(channel_messages)
                    total_messages += len(channel_messages)
                    print(f"✅ Exported {len(channel_messages)} messages from {channel.name} (including threads)")
                    
                except Exception as e:
                    print(f"❌ Error exporting {channel.name}: {str(e)}")
                    continue

            # Write all messages to a single CSV file
            csv_path = os.path.join("csv_files", "chat_history.csv")
            try:
                with open(csv_path, "w", encoding="utf-8", newline='') as f:
                    writer = csv.DictWriter(f, fieldnames=[
                        "channel_name", "channel_id", "thread_name","thread_id",
                        "message_id", "author", "chat_text", "created_at"
                    ])
                    writer.writeheader()
                    writer.writerows(all_messages)
                
                print(f"✅ Wrote {csv_path} ({total_messages} messages total)")
            except Exception as e:
                print(f"❌ Error writing CSV file: {str(e)}")

            await client.close()

        await client.start(self.token)

    async def run_etl_pipeline(self) -> None:
        """
        Run the complete ETL pipeline: export chat history to CSV.
        
        This method orchestrates the extraction process:
        - Directly exports all messages to CSV
        
        The pipeline ensures that:
        - All data is extracted in a single step
        - Progress is reported to the user
        """
        print("🔄 Starting Discord ETL pipeline...")
        
        # Export chat history directly to CSV
        print("▶️ Exporting chat history...")
        await self.export_chat_history()
        
        print("✅ ETL pipeline completed successfully")

    