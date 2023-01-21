import argparse
from configparser import ConfigParser

import psycopg2


def get_config(filename='config.ini', section='postgresql'):
    # create a parser
    parser = ConfigParser()
    # read config file
    parser.read(filename)

    # get section, default to postgresql
    db_config = {}
    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            db_config[param[0]] = param[1]
    else:
        raise Exception('Section {0} not found in the {1} file'.format(section, filename))

    return db_config


def perform_query(movie_name):
    # read connection parameters
    params = get_config("top250_movies_db.ini")

    with psycopg2.connect(**params) as conn:
        cur: psycopg2._psycopg.cursor = conn.cursor()

        query = f"select * from imdb_top where movie_name ilike '{movie_name}';"
        print(f"going to execute: {query}")
        cur.execute(query)
        results = cur.fetchall()
        return results


def perform_query(movie_name):
    # read connection parameters
    params = get_config("top250_movies_db.ini")

    with psycopg2.connect(**params) as conn:
        cur: psycopg2._psycopg.cursor = conn.cursor()

        query = "select * from imdb_top where movie_name ilike %s;"
        print(f"going to execute: {query}")
        cur.execute(query, (movie_name,))
        results = cur.fetchall()
        return results


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('movie_name')
    parser.add_argument('rating')

    args = parser.parse_args()
    results = perform_query(args.movie_name)
    result = perform_query((args.rating))
    print(results)
