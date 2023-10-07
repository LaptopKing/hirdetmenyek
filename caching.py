#!/usr/bin/env python3

from modules import logger, announcements, backup, save

if __name__ == '__main__':
    log = logger.Logger('caching' if __name__ == '__main__' else __name__)

    try:

        dbName = 'hirdetmenyek'

        if (not backup.backup(dbName)):
            log.warning(f'There is no {dbName} database to backup from')

        data = announcements.getAnnouncements()
        log.info('Get announcements from https://hirdetmenyek.gov.hu/api/hirdetmenyek')

        collectionName = 'Hirdetmenyek'

        save.save(dbName, collectionName, data)
        log.info(f'Announcements saved to Collection {collectionName} in Database {dbName}')

    except Exception:
        log.exception(Exception)
