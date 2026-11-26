import logging
from psycopg.rows import dict_row
from psycopg import AsyncConnection
from langgraph.checkpoint.postgres.aio import AsyncPostgresSaver
from app.core.config import settings

logger = logging.getLogger(__name__)
_connection = None
_checkpointer = None

async def initialize_checkpointer():
    global _connection, _checkpointer
    if not settings.workflow_checkpoint_enabled:
        logger.warning("LangGraph checkpointing disabled")
        return None
    if _checkpointer is not None:
        return _checkpointer
    url = settings.database_url
    if url.startswith("postgres://"):
        url = "postgresql://" + url[len("postgres://"):]
    url = url.replace("postgresql+psycopg://", "postgresql://")
    _connection = await AsyncConnection.connect(url, autocommit=True, row_factory=dict_row)
    _checkpointer = AsyncPostgresSaver(_connection)
    await _checkpointer.setup()
    logger.info("LangGraph async PostgreSQL checkpointer initialized")
    return _checkpointer

def get_checkpointer():
    return _checkpointer

async def close_checkpointer():
    global _connection, _checkpointer
    if _connection is not None:
        await _connection.close()
    _connection = None
    _checkpointer = None
