"""
Seed data to the database.
"""

import asyncio
import typing as tp

import asyncpg
from faker import Faker

from threepeat.log import get_logger
from threepeat.settings import LOCALE, SEED_COUNT, db_connection_string

logger = get_logger(__name__)


async def db_connect() -> tp.Coroutine:
    conn = await asyncpg.connect(db_connection_string())
    return conn


def get_users(count: int = 10) -> list[tp.Tuple[str, str]]:
    f = Faker(LOCALE)
    return [(f.first_name(), f.password(4)) for _ in range(count)]


async def main():
    logger.info(f'Creating {SEED_COUNT:_} users.')
    users = get_users(SEED_COUNT)

    conn = await db_connect()

    stmt = 'INSERT INTO users (name, password) VALUES ($1, $2)'
    logger.info('Inserting users.')
    await conn.executemany(stmt, users)
    logger.info('Done.')

    await conn.close()


asyncio.run(main())
