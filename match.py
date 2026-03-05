{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "74ec35ad-c4bb-492a-9048-a52b378b0bac",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "a92b690e-258c-4322-be59-85505a9908ab",
   "metadata": {},
   "outputs": [],
   "source": [
    "import redis\n",
    "\n",
    "r = redis.Redis(host='localhost', port=6379, decode_responses=True)\n",
    "class Match:\n",
    "    def __init__(self, id, domicile, exterieur, date_heure,\n",
    "                 statut, score, competition, stade, arbitre):\n",
    "        self.id = id\n",
    "        self.domicile = domicile\n",
    "        self.exterieur = exterieur\n",
    "        self.date_heure = date_heure\n",
    "        self.statut = statut\n",
    "        self.score = score\n",
    "        self.competition = competition\n",
    "        self.stade = stade\n",
    "        self.arbitre = arbitre\n",
    "    def save(self, ttl=3600):\n",
    "        \"\"\"Sauvegarder le match dans Redis avec TTL\"\"\"\n",
    "        key = f\"match:{self.id}\"\n",
    "        r.hset(key, mapping={\n",
    "            \"id\": self.id,\n",
    "            \"domicile\": self.domicile,\n",
    "            \"exterieur\": self.exterieur,\n",
    "            \"date_heure\": self.date_heure,\n",
    "            \"statut\": self.statut,\n",
    "            \"score\": self.score,\n",
    "            \"competition\": self.competition,\n",
    "            \"stade\": self.stade,\n",
    "            \"arbitre\": self.arbitre\n",
    "        })\n",
    "        r.expire(key, ttl)\n",
    "        r.sadd(f\"competition:{self.competition}\", self.id)\n",
    "        print(f\"✅ Match {self.id} ajouté avec succès\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "0fb02efa-b90a-4e16-9a75-80ab31d4e157",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "✅ Match 001 ajouté avec succès\n"
     ]
    }
   ],
   "source": [
    "# Créer un match\n",
    "match1 = Match(\n",
    "    id=\"001\",\n",
    "    domicile=\"Maroc\",\n",
    "    exterieur=\"France\",\n",
    "    date_heure=\"2025-12-25 20:00\",\n",
    "    statut=\"prévu\",\n",
    "    score=\"0-0\",\n",
    "    competition=\"Coupe du Monde\",\n",
    "    stade=\"Stade de Marrakech\",\n",
    "    arbitre=\"Mr. Dupont\"\n",
    ")\n",
    "\n",
    "# Sauvegarder le match dans Redis\n",
    "match1.save()\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "d7ee93db-fc7d-4fce-a666-2a230ce547bb",
   "metadata": {},
   "outputs": [
    {
     "ename": "NameError",
     "evalue": "name 'null' is not defined",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mNameError\u001b[0m                                 Traceback (most recent call last)",
      "Cell \u001b[1;32mIn[8], line 2\u001b[0m\n\u001b[0;32m      1\u001b[0m \u001b[38;5;28;01mimport\u001b[39;00m\u001b[38;5;250m \u001b[39m\u001b[38;5;21;01mredis\u001b[39;00m\n\u001b[1;32m----> 2\u001b[0m \u001b[38;5;28;01mfrom\u001b[39;00m\u001b[38;5;250m \u001b[39m\u001b[38;5;21;01mmatch\u001b[39;00m\u001b[38;5;250m \u001b[39m\u001b[38;5;28;01mimport\u001b[39;00m Match\n\u001b[0;32m      4\u001b[0m r \u001b[38;5;241m=\u001b[39m redis\u001b[38;5;241m.\u001b[39mRedis(decode_responses\u001b[38;5;241m=\u001b[39m\u001b[38;5;28;01mTrue\u001b[39;00m)\n\u001b[0;32m      6\u001b[0m match1 \u001b[38;5;241m=\u001b[39m Match(\n\u001b[0;32m      7\u001b[0m     \u001b[38;5;28mid\u001b[39m\u001b[38;5;241m=\u001b[39m\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m001\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m      8\u001b[0m     domicile\u001b[38;5;241m=\u001b[39m\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mMaroc\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[1;32m   (...)\u001b[0m\n\u001b[0;32m     15\u001b[0m     arbitre\u001b[38;5;241m=\u001b[39m\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mMr. Dupont\u001b[39m\u001b[38;5;124m\"\u001b[39m\n\u001b[0;32m     16\u001b[0m )\n",
      "File \u001b[1;32m~\\match.py:86\u001b[0m\n\u001b[0;32m      1\u001b[0m {\n\u001b[0;32m      2\u001b[0m  \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mcells\u001b[39m\u001b[38;5;124m\"\u001b[39m: [\n\u001b[0;32m      3\u001b[0m   {\n\u001b[0;32m      4\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mcell_type\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mcode\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m      5\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mexecution_count\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;241m5\u001b[39m,\n\u001b[0;32m      6\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mid\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m74ec35ad-c4bb-492a-9048-a52b378b0bac\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m      7\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mmetadata\u001b[39m\u001b[38;5;124m\"\u001b[39m: {},\n\u001b[0;32m      8\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124moutputs\u001b[39m\u001b[38;5;124m\"\u001b[39m: [],\n\u001b[0;32m      9\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124msource\u001b[39m\u001b[38;5;124m\"\u001b[39m: []\n\u001b[0;32m     10\u001b[0m   },\n\u001b[0;32m     11\u001b[0m   {\n\u001b[0;32m     12\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mcell_type\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mcode\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m     13\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mexecution_count\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;241m6\u001b[39m,\n\u001b[0;32m     14\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mid\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124ma92b690e-258c-4322-be59-85505a9908ab\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m     15\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mmetadata\u001b[39m\u001b[38;5;124m\"\u001b[39m: {},\n\u001b[0;32m     16\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124moutputs\u001b[39m\u001b[38;5;124m\"\u001b[39m: [],\n\u001b[0;32m     17\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124msource\u001b[39m\u001b[38;5;124m\"\u001b[39m: [\n\u001b[0;32m     18\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mimport redis\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m     19\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m     20\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mr = redis.Redis(host=\u001b[39m\u001b[38;5;124m'\u001b[39m\u001b[38;5;124mlocalhost\u001b[39m\u001b[38;5;124m'\u001b[39m\u001b[38;5;124m, port=6379, decode_responses=True)\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m     21\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mclass Match:\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m     22\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m    def __init__(self, id, domicile, exterieur, date_heure,\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m     23\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m                 statut, score, competition, stade, arbitre):\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m     24\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m        self.id = id\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m     25\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m        self.domicile = domicile\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m     26\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m        self.exterieur = exterieur\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m     27\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m        self.date_heure = date_heure\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m     28\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m        self.statut = statut\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m     29\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m        self.score = score\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m     30\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m        self.competition = competition\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m     31\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m        self.stade = stade\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m     32\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m        self.arbitre = arbitre\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m     33\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m    def save(self, ttl=3600):\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m     34\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m        \u001b[39m\u001b[38;5;130;01m\\\"\u001b[39;00m\u001b[38;5;130;01m\\\"\u001b[39;00m\u001b[38;5;130;01m\\\"\u001b[39;00m\u001b[38;5;124mSauvegarder le match dans Redis avec TTL\u001b[39m\u001b[38;5;130;01m\\\"\u001b[39;00m\u001b[38;5;130;01m\\\"\u001b[39;00m\u001b[38;5;130;01m\\\"\u001b[39;00m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m     35\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m        key = f\u001b[39m\u001b[38;5;130;01m\\\"\u001b[39;00m\u001b[38;5;124mmatch:\u001b[39m\u001b[38;5;132;01m{self.id}\u001b[39;00m\u001b[38;5;130;01m\\\"\u001b[39;00m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m     36\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m        r.hset(key, mapping=\u001b[39m\u001b[38;5;124m{\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m     37\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m            \u001b[39m\u001b[38;5;130;01m\\\"\u001b[39;00m\u001b[38;5;124mid\u001b[39m\u001b[38;5;130;01m\\\"\u001b[39;00m\u001b[38;5;124m: self.id,\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m     38\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m            \u001b[39m\u001b[38;5;130;01m\\\"\u001b[39;00m\u001b[38;5;124mdomicile\u001b[39m\u001b[38;5;130;01m\\\"\u001b[39;00m\u001b[38;5;124m: self.domicile,\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m     39\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m            \u001b[39m\u001b[38;5;130;01m\\\"\u001b[39;00m\u001b[38;5;124mexterieur\u001b[39m\u001b[38;5;130;01m\\\"\u001b[39;00m\u001b[38;5;124m: self.exterieur,\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m     40\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m            \u001b[39m\u001b[38;5;130;01m\\\"\u001b[39;00m\u001b[38;5;124mdate_heure\u001b[39m\u001b[38;5;130;01m\\\"\u001b[39;00m\u001b[38;5;124m: self.date_heure,\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m     41\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m            \u001b[39m\u001b[38;5;130;01m\\\"\u001b[39;00m\u001b[38;5;124mstatut\u001b[39m\u001b[38;5;130;01m\\\"\u001b[39;00m\u001b[38;5;124m: self.statut,\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m     42\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m            \u001b[39m\u001b[38;5;130;01m\\\"\u001b[39;00m\u001b[38;5;124mscore\u001b[39m\u001b[38;5;130;01m\\\"\u001b[39;00m\u001b[38;5;124m: self.score,\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m     43\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m            \u001b[39m\u001b[38;5;130;01m\\\"\u001b[39;00m\u001b[38;5;124mcompetition\u001b[39m\u001b[38;5;130;01m\\\"\u001b[39;00m\u001b[38;5;124m: self.competition,\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m     44\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m            \u001b[39m\u001b[38;5;130;01m\\\"\u001b[39;00m\u001b[38;5;124mstade\u001b[39m\u001b[38;5;130;01m\\\"\u001b[39;00m\u001b[38;5;124m: self.stade,\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m     45\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m            \u001b[39m\u001b[38;5;130;01m\\\"\u001b[39;00m\u001b[38;5;124marbitre\u001b[39m\u001b[38;5;130;01m\\\"\u001b[39;00m\u001b[38;5;124m: self.arbitre\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m     46\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m        })\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m     47\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m        r.expire(key, ttl)\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m     48\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m        r.sadd(f\u001b[39m\u001b[38;5;130;01m\\\"\u001b[39;00m\u001b[38;5;124mcompetition:\u001b[39m\u001b[38;5;132;01m{self.competition}\u001b[39;00m\u001b[38;5;130;01m\\\"\u001b[39;00m\u001b[38;5;124m, self.id)\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m     49\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m        print(f\u001b[39m\u001b[38;5;130;01m\\\"\u001b[39;00m\u001b[38;5;124m✅ Match \u001b[39m\u001b[38;5;132;01m{self.id}\u001b[39;00m\u001b[38;5;124m ajouté avec succès\u001b[39m\u001b[38;5;130;01m\\\"\u001b[39;00m\u001b[38;5;124m)\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m\n\u001b[0;32m     50\u001b[0m    ]\n\u001b[0;32m     51\u001b[0m   },\n\u001b[0;32m     52\u001b[0m   {\n\u001b[0;32m     53\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mcell_type\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mcode\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m     54\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mexecution_count\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;241m7\u001b[39m,\n\u001b[0;32m     55\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mid\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m0fb02efa-b90a-4e16-9a75-80ab31d4e157\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m     56\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mmetadata\u001b[39m\u001b[38;5;124m\"\u001b[39m: {},\n\u001b[0;32m     57\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124moutputs\u001b[39m\u001b[38;5;124m\"\u001b[39m: [\n\u001b[0;32m     58\u001b[0m     {\n\u001b[0;32m     59\u001b[0m      \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mname\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mstdout\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m     60\u001b[0m      \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124moutput_type\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mstream\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m     61\u001b[0m      \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mtext\u001b[39m\u001b[38;5;124m\"\u001b[39m: [\n\u001b[0;32m     62\u001b[0m       \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m✅ Match 001 ajouté avec succès\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m\n\u001b[0;32m     63\u001b[0m      ]\n\u001b[0;32m     64\u001b[0m     }\n\u001b[0;32m     65\u001b[0m    ],\n\u001b[0;32m     66\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124msource\u001b[39m\u001b[38;5;124m\"\u001b[39m: [\n\u001b[0;32m     67\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m# Créer un match\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m     68\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mmatch1 = Match(\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m     69\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m    id=\u001b[39m\u001b[38;5;130;01m\\\"\u001b[39;00m\u001b[38;5;124m001\u001b[39m\u001b[38;5;130;01m\\\"\u001b[39;00m\u001b[38;5;124m,\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m     70\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m    domicile=\u001b[39m\u001b[38;5;130;01m\\\"\u001b[39;00m\u001b[38;5;124mMaroc\u001b[39m\u001b[38;5;130;01m\\\"\u001b[39;00m\u001b[38;5;124m,\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m     71\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m    exterieur=\u001b[39m\u001b[38;5;130;01m\\\"\u001b[39;00m\u001b[38;5;124mFrance\u001b[39m\u001b[38;5;130;01m\\\"\u001b[39;00m\u001b[38;5;124m,\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m     72\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m    date_heure=\u001b[39m\u001b[38;5;130;01m\\\"\u001b[39;00m\u001b[38;5;124m2025-12-25 20:00\u001b[39m\u001b[38;5;130;01m\\\"\u001b[39;00m\u001b[38;5;124m,\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m     73\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m    statut=\u001b[39m\u001b[38;5;130;01m\\\"\u001b[39;00m\u001b[38;5;124mprévu\u001b[39m\u001b[38;5;130;01m\\\"\u001b[39;00m\u001b[38;5;124m,\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m     74\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m    score=\u001b[39m\u001b[38;5;130;01m\\\"\u001b[39;00m\u001b[38;5;124m0-0\u001b[39m\u001b[38;5;130;01m\\\"\u001b[39;00m\u001b[38;5;124m,\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m     75\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m    competition=\u001b[39m\u001b[38;5;130;01m\\\"\u001b[39;00m\u001b[38;5;124mCoupe du Monde\u001b[39m\u001b[38;5;130;01m\\\"\u001b[39;00m\u001b[38;5;124m,\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m     76\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m    stade=\u001b[39m\u001b[38;5;130;01m\\\"\u001b[39;00m\u001b[38;5;124mStade de Marrakech\u001b[39m\u001b[38;5;130;01m\\\"\u001b[39;00m\u001b[38;5;124m,\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m     77\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m    arbitre=\u001b[39m\u001b[38;5;130;01m\\\"\u001b[39;00m\u001b[38;5;124mMr. Dupont\u001b[39m\u001b[38;5;130;01m\\\"\u001b[39;00m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m     78\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m)\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m     79\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m     80\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m# Sauvegarder le match dans Redis\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m     81\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mmatch1.save()\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m\n\u001b[0;32m     82\u001b[0m    ]\n\u001b[0;32m     83\u001b[0m   },\n\u001b[0;32m     84\u001b[0m   {\n\u001b[0;32m     85\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mcell_type\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mcode\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[1;32m---> 86\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mexecution_count\u001b[39m\u001b[38;5;124m\"\u001b[39m: null,\n\u001b[0;32m     87\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mid\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124md7ee93db-fc7d-4fce-a666-2a230ce547bb\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m     88\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mmetadata\u001b[39m\u001b[38;5;124m\"\u001b[39m: {},\n\u001b[0;32m     89\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124moutputs\u001b[39m\u001b[38;5;124m\"\u001b[39m: [],\n\u001b[0;32m     90\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124msource\u001b[39m\u001b[38;5;124m\"\u001b[39m: []\n\u001b[0;32m     91\u001b[0m   }\n\u001b[0;32m     92\u001b[0m  ],\n\u001b[0;32m     93\u001b[0m  \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mmetadata\u001b[39m\u001b[38;5;124m\"\u001b[39m: {\n\u001b[0;32m     94\u001b[0m   \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mkernelspec\u001b[39m\u001b[38;5;124m\"\u001b[39m: {\n\u001b[0;32m     95\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mdisplay_name\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mPython 3 (ipykernel)\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m     96\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mlanguage\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mpython\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m     97\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mname\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mpython3\u001b[39m\u001b[38;5;124m\"\u001b[39m\n\u001b[0;32m     98\u001b[0m   },\n\u001b[0;32m     99\u001b[0m   \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mlanguage_info\u001b[39m\u001b[38;5;124m\"\u001b[39m: {\n\u001b[0;32m    100\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mcodemirror_mode\u001b[39m\u001b[38;5;124m\"\u001b[39m: {\n\u001b[0;32m    101\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mname\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mipython\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m    102\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mversion\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;241m3\u001b[39m\n\u001b[0;32m    103\u001b[0m    },\n\u001b[0;32m    104\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mfile_extension\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m.py\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m    105\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mmimetype\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mtext/x-python\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m    106\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mname\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mpython\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m    107\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mnbconvert_exporter\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mpython\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m    108\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mpygments_lexer\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mipython3\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m    109\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mversion\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m3.13.5\u001b[39m\u001b[38;5;124m\"\u001b[39m\n\u001b[0;32m    110\u001b[0m   }\n\u001b[0;32m    111\u001b[0m  },\n\u001b[0;32m    112\u001b[0m  \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mnbformat\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;241m4\u001b[39m,\n\u001b[0;32m    113\u001b[0m  \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mnbformat_minor\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;241m5\u001b[39m\n\u001b[0;32m    114\u001b[0m }\n",
      "\u001b[1;31mNameError\u001b[0m: name 'null' is not defined"
     ]
    }
   ],
   "source": [
    "import redis\n",
    "from match import Match\n",
    "\n",
    "r = redis.Redis(decode_responses=True)\n",
    "\n",
    "match1 = Match(\n",
    "    id=\"001\",\n",
    "    domicile=\"Maroc\",\n",
    "    exterieur=\"France\",\n",
    "    date_heure=\"2025-12-25 20:00\",\n",
    "    statut=\"prévu\",\n",
    "    score=\"0-0\",\n",
    "    competition=\"Coupe du Monde\",\n",
    "    stade=\"Stade de Marrakech\",\n",
    "    arbitre=\"Mr. Dupont\"\n",
    ")\n",
    "\n",
    "# Ajouter le match\n",
    "match1.save()\n",
    "\n",
    "# Publier l'événement\n",
    "canal = f\"canal:{match1.competition}\"\n",
    "r.publish(canal, match1.id)\n",
    "\n",
    "print(f\"📢 Match publié sur {canal}\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "eadf51e9-7505-4b86-9af8-37f2f4c83aa9",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.13.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
