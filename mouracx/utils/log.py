import os
import logging
from logging import handlers

LOG_LEVEL = os.getenv("LOG_LEVEL", "WARNING").upper()
log = logging.getLogger("mouracx")

fmt = logging.Formatter(
        '%(asctime)s    %(name)s    %(levelname)s   l:%(lineno)d    f:%(filename)s: %(message)s'
    )

def get_logger(logfile="mouracx.log"):
    """Returns a configured logger."""

    fh = handlers.RotatingFileHandler(
        logfile, 
        maxBytes=300, # 10**6, 
        backupCount=10,
    )
    fh.setLevel(LOG_LEVEL)
    fh.setFormatter(fmt)
    log.addHandler(fh)
    return log


    """
    log.debug("Mensagem pro dev, qa, sysadmin")
    log.info("Mensagem geral para usuários")
    log.warning("Aviso que não causa erro")
    log.error("Erro que afeta uma unica execução")
    log.critical("Erro geral ex: banco de dados sumiu")
    """
