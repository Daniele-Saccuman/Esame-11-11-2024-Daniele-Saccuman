from database.DB_connect import DBConnect
from model.state import State
from model.sighting import Sighting


class DAO():
    def __init__(self):
        pass


    @staticmethod
    def get_all_states():
        cnx = DBConnect.get_connection()
        result = []
        if cnx is None:
            print("Connessione fallita")
        else:
            cursor = cnx.cursor(dictionary=True)
            query = """select * 
                    from state s"""
            cursor.execute(query)

            for row in cursor:
                result.append(
                    State(**row))

            cursor.close()
            cnx.close()
        return result

    @staticmethod
    def get_all_sightings(anno, minDur, maxDur):
        cnx = DBConnect.get_connection()
        result = []
        if cnx is None:
            print("Connessione fallita")
        else:
            cursor = cnx.cursor(dictionary=True)
            query = """select s.*
                        from sighting s 
                        where year(s.`datetime`) = %s
                        and s.duration  > %s
                        and s.duration < %s """
            cursor.execute(query, (anno, minDur, maxDur))

            for row in cursor:
                result.append(Sighting(**row))
            cursor.close()
            cnx.close()
        return result

    @staticmethod
    def getAllEdges(anno, minDur, maxDur):
        cnx = DBConnect.get_connection()
        result = []
        if cnx is None:
            print("Connessione fallita")
        else:
            cursor = cnx.cursor(dictionary=True)
            query = """select s1.id as id1, s1.duration as dur1, s2.id as id2,  s2.duration as dur2
                        from sighting s1, sighting s2  
                        where year(s1.`datetime`) = %s
                        and year(s2.`datetime`) = %s
                        and s1.id <> s2.id
                        and s1.duration  > %s
                        and s1.duration < %s
                        and s2.duration  > %s
                        and s2.duration < %s
                        and s1.shape = s2.shape """
            cursor.execute(query, (anno, anno, minDur, maxDur, minDur, maxDur))

            for row in cursor:
                result.append((row["id1"], row["dur1"], row["id2"], row["dur2"]))
            cursor.close()
            cnx.close()
        return result

    def getAllDurate(anno, minDur, maxDur):
        cnx = DBConnect.get_connection()
        result = []
        if cnx is None:
            print("Connessione fallita")
        else:
            cursor = cnx.cursor(dictionary=True)
            query = """select distinct (s.duration) as durata, count(s.id) as nodi
                        from sighting s 
                        where year(s.`datetime`) = %s
                        and s.duration  > %s
                        and s.duration < %s
                        group by durata
                        order by durata """
            cursor.execute(query, (anno, minDur, maxDur,))

            for row in cursor:
                result.append((row["durata"], row["nodi"]))
            cursor.close()
            cnx.close()
        return result

    def getMedia(anno, minDur, maxDur):
        cnx = DBConnect.get_connection()
        result = []
        if cnx is None:
            print("Connessione fallita")
        else:
            cursor = cnx.cursor(dictionary=True)
            query = """select avg(s.duration) as media
                        from sighting s 
                        where year(s.`datetime`) = %s
                        and s.duration  > %s
                        and s.duration < %s """
            cursor.execute(query, (anno, minDur, maxDur,))

            for row in cursor:
                result.append(row["media"])
            cursor.close()
            cnx.close()
        return result

    @staticmethod
    def getDurata():
        cnx = DBConnect.get_connection()
        result = []
        if cnx is None:
            print("Connessione fallita")
        else:
            cursor = cnx.cursor(dictionary=True)
            query = """select min(s.duration) as minDur, max(s.duration) as maxDur
                        from sighting s """
            cursor.execute(query)

            for row in cursor:
                result.append((row["minDur"], row["maxDur"]))
            cursor.close()
            cnx.close()
            return result
    @staticmethod
    def getAllYears():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """select distinct year(s.`datetime`) as anno
                    from sighting s
                    order by anno desc"""

        cursor.execute(query)

        for row in cursor:
            result.append(row['anno'])

        cursor.close()
        conn.close()
        return result





