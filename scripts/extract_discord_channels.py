import asyncio
from utils.extractor import DiscordExtractor

async def main():
    """Run the Discord channel extraction."""
    try:
        extractor = DiscordExtractor()
        await extractor.export_channels()
    except Exception as e:
        print(f"❌ Error running channel extraction: {str(e)}")
        raise

if __name__ == "__main__":
    asyncio.run(main())
