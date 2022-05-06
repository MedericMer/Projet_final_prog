####################################################################################
###  420-2G2 - Programmation orientée objet
###  Travail: Projet Final
###  Nom: Médéric Mercier
###  No étudiant: 2174594
###  No Groupe: 00001
###  Description du fichier: class Docteur du projet Clinique
####################################################################################
from Intervenant import *


class Docteur (Intervenant):
    """

    """

    def __init__(self, p_num_intervenant: str = "", p_nom_intervenant: str = "", p_nb_annee_experience: int = 0,
                 p_Specialite: str = "", p_Superviseur: bool = False):
        """

        :param p_num_intervenant:
        :param p_nom_intervenant:
        :param p_nb_annee_experience:
        :param p_Specialite:
        :param p_Superviseur:
        """
        Intervenant.__init__(self, p_num_intervenant, p_nom_intervenant, p_nb_annee_experience)
        self.Specialite = p_Specialite
        self.Superviseur = p_Superviseur

    def __str__(self):
