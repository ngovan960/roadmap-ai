"""SQLite database connection and initialization."""

import aiosqlite
from pathlib import Path
from backend.config import settings

# Ensure data directory exists
Path("data").mkdir(parents=True, exist_ok=True)

DB_PATH = settings.db_path

async def get_db():
    """Get database connection as async context manager."""
    db = await aiosqlite.connect(DB_PATH)
    db.row_factory = aiosqlite.Row
    try:
        yield db
    finally:
        await db.close()

async def init_database():
    """Initialize database with required tables."""
    async with aiosqlite.connect(DB_PATH) as db:
        # Create roadmaps table
        await db.execute("""
            CREATE TABLE IF NOT EXISTS roadmaps (
                id TEXT PRIMARY KEY,
                slug TEXT UNIQUE NOT NULL,
                
                -- Input
                age INTEGER NOT NULL,
                industry TEXT NOT NULL,
                industry_name TEXT NOT NULL,
                level TEXT NOT NULL,
                goal TEXT NOT NULL,
                duration_months INTEGER NOT NULL,
                current_job TEXT,
                hours_per_day TEXT DEFAULT '3-4',
                learning_style TEXT,
                
                -- Level 1: Roadmap overview
                overview TEXT,
                total_weeks INTEGER,
                total_tasks INTEGER,
                total_hours INTEGER,
                salary_junior TEXT,
                salary_mid TEXT,
                salary_senior TEXT,
                competitive_advantage TEXT,
                market_demand TEXT,
                
                -- Full roadmap JSON (Phases → Modules → Tasks → Resources)
                roadmap_json TEXT,
                
                -- Metadata
                ai_model TEXT DEFAULT 'mimo-v2.5',
                ai_tokens_used INTEGER,
                generation_time_ms INTEGER,
                view_count INTEGER DEFAULT 0,
                share_count INTEGER DEFAULT 0,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)
        
        # Create indexes
        await db.execute("CREATE INDEX IF NOT EXISTS idx_roadmaps_slug ON roadmaps(slug)")
        await db.execute("CREATE INDEX IF NOT EXISTS idx_roadmaps_industry ON roadmaps(industry)")
        
        await db.commit()
        print(f"Database initialized at {DB_PATH}")
