import asyncio
from utils.extractor import DiscordExtractor

async def main():
    """Run the complete Discord ETL pipeline."""
    try:
        extractor = DiscordExtractor()
        await extractor.run_etl_pipeline()
    except Exception as e:
        print(f"❌ Error running ETL pipeline: {str(e)}")
        raise

if __name__ == "__main__":
    asyncio.run(main())

