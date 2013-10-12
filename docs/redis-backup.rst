============
Redis Backup
============

Using crontab
=============

.. warning::
    
    This is untested.

::
    
    # This is set in redis config.
    DB="/path/to/redis/dump.rdb"
    DEST="/path/to/backup/directory";

    # copy only if file has been modified in the last 24 hours.
    if [[ -n $(find $DB -mtime -1) ]]; then
        cp -b $DB "$DEST/dump.rdb.$(date '+%j')";
    fi;

::
    
    0  0 * * * redis-cli bgsave
    15 0 * * * DB="/path/to/redis/dump.rdb"; DEST="/path/to/backup/directory"; if [[ -n $(find $DB -mtime -1) ]]; then cp -b $DB "$DEST/dump.rdb.$(date '+%j')"; fi;
