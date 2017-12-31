sudo sudo -u postgres psql dsmrreader -t -c "SELECT pg_size_pretty( pg_database_size('dsmrreader') );"
