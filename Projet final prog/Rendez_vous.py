####################################################################################
###  420-2G2 - Programmation orientée objet
###  Travail: Projet Final
###  Nom: Médéric Mercier
###  No étudiant: 2174594
###  No Groupe: 00001
###  Description du fichier: classe Rendez-vous du projet Clinique
####################################################################################
from Intervenant import *
from Patient import *


class Rendez_vous:
    """

    """
    def __init__(self, p_num_rdv: str = "", p_jour_rdv: str = "", p_Salle_rdv: str = ""):
        """

        :param p_num_rdv:
        :param p_jour_rdv:
        :param p_Salle_rdv:
        """
        self.__num_rdv = p_num_rdv
        self.__jour_rdv = p_jour_rdv
        self.Salle_rdv = p_Salle_rdv

###################
####    STR    ####
###################
    def __str__(self):
        """

        :return:
        """
        chaineRDV = " "*60+"\n"+"*"*60+"\n\n"+" Le numéro du rendez-vous est :"+self.__num_rdv+"\n"+\
            "Le jour du rendez-vous est : "+self.__jour_rdv+" prochain"+"\n"+"La salle du rendez-vous est : "+\
            self.Salle_rdv+"\n\n"+"*"*60
        return chaineRDV

#############################################################################################################

    def _get_num_rdv(self):
        """

        :return:
        """
        return self.__num_rdv

    def _set_num_rdv(self, p_num_rdv):
        """

        :param p_num_rdv:
        :return:
        """
        if p_num_rdv.isnumeric() and len(p_num_rdv) == 5:
            self.__num_rdv = p_num_rdv

    NumRdv = property(_get_num_rdv, _set_num_rdv)
#############################################################################################################

    def _get_jour_rdv(self):
        """

        :return:
        """
        return self.__jour_rdv

    def _set_jour_rdv(self, p_jour_rdv):
        """

        :param p_jour_rdv:
        :return:
        """
        if p_jour_rdv == "lundi" or "mardi" or "mercredi" or "jeudi" or "vendredi":
            self.__jour_rdv = p_jour_rdv

    JourRdv = property(_get_jour_rdv, _set_jour_rdv)

