####################################################################################
###  420-2G2 - Programmation orientée objet
###  Travail: Projet Final
###  Nom: Médéric Mercier
###  No étudiant: 2174594
###  No Groupe: 00001
###  Description du fichier: classe Intervenant du projet Clinique
####################################################################################

class Intervenant():
    def __init__(self, p_num_intervenant: str = "", p_nom_intervenant: str = "", p_nb_annee_experience: int = 0):
        """

        :param p_num_intervenant:
        :param p_nom_intervenant:
        :param p_nb_annee_experience:
        """
        self.__num_intervenant = p_num_intervenant
        self.__nom_intervevant = p_nom_intervenant
        self.__nb_annee_experience = p_nb_annee_experience

    def __str__(self):
        """

        :return:
        """
        chanieINTERVENANT = " " * 60 + "\n" + "*" * 60 + "\n\n" + " Le numéro de l'intervenant est :" +\
                    self.__num_intervenant + "\n" + \
                    "Le nom de l'intervenant est : " + self.__nom_intervevant + "\n" + "Le nombre d'années " \
                    "d'expérience de l'intervenant est : "+str(self.__nb_annee_experience)+ "\n\n" + "*" * 60
        return chanieINTERVENANT

    #############################################################################################################
    def _get_num_intervenant(self):
        """

        :return:
        """
        return self.__num_intervenant

    def _set_num_intervenant(self, p_num_intervenant):
        """

        :param p_num_intervenant:
        :return:
        """
        if p_num_intervenant.isnumeric() and len(p_num_intervenant) == 5:
            self.__num_intervenant = p_num_intervenant

    NumIntervenant = property(_get_num_intervenant, _set_num_intervenant)

    #############################################################################################################
    def _get_nom_intervenant(self):
        """

        :return:
        """
        return self.__nom_intervevant

    def _set_nom_intervenant(self, p_nom_intervenant):
        """

        :param p_nom_intervenant:
        :return:
        """
        if p_nom_intervenant.isalpha() and len(p_nom_intervenant) <= 20:
            self.__nom_intervevant = p_nom_intervenant

    NomIntervenant = property(_get_nom_intervenant, _set_nom_intervenant)

    #############################################################################################################
    def _get_nb_annee_experience(self):
        """

        :return:
        """
        return self.__nb_annee_experience

    def _set_nb_annee_experience(self, p_nb_annee_experience):
        """

        :param p_nb_annee_experience:
        :return:
        """
        if p_nb_annee_experience < 50:
            self.__nb_annee_experience = p_nb_annee_experience

    NbAnneeExperience = property(_get_nb_annee_experience, _set_nb_annee_experience)
