####################################################################################
###  420-2G2 - Programmation orientée objet
###  Travail: Projet Final
###  Nom: Médéric Mercier
###  No étudiant: 2174594
###  No Groupe: 00001
###  Description du fichier: classe Infirmiere du projet Clinique
####################################################################################
from Intervenant import *


class Infirmiere(Intervenant):
    """

    """

    def __init__(self, p_num_intervenant: str = "", p_nom_intervenant: str = "", p_nb_annee_experience: int = 0,
                 p_Quart_travail: str = ""):
        """

        :param p_num_intervenant:
        :param p_nom_intervenant:
        :param p_nb_annee_experience:
        :param p_Quart_travail:
        """
        Intervenant.__init__(self, p_num_intervenant, p_nom_intervenant, p_nb_annee_experience)
        self.Quart_travail = p_Quart_travail

    def __str__(self):
        """

        :return:
        """
        chaineINFIRMIERE = " " * 60 + "\n" + "*" * 60 + "\n\n" + " Le quart de travail de l'infirmière est : " + \
                           self.Quart_travail + "\n\n" + "*" * 60
        return chaineINFIRMIERE
