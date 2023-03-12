"""
Fetch data from the database.
"""

import asyncio
from datetime import datetime as dt
from zoneinfo import ZoneInfo

import asyncpg

from threepeat import settings
from threepeat.log import get_logger

logger = get_logger(__name__)


async def run():
    conn = await asyncpg.connect(
        user=settings.DB_USER,
        password=settings.DB_PASS,
        database=settings.DB_SCHEMA,
        host=settings.DB_HOST,
    )
    rows = await conn.fetch('SELECT * FROM users LIMIT 1')
    await conn.close()

    for row in rows:
        created = row['created']
        createdtz = dt.astimezone(created, ZoneInfo(settings.TZ))

        logger.info(f'{row=}')
        logger.info(f'{created=}')
        logger.info(f'{createdtz=}')
        logger.info(f'{createdtz=:%Y-%m-%d %H:%M:%S}')


asyncio.run(run(), debug=False)
