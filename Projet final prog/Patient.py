####################################################################################
###  420-2G2 - Programmation orientée objet
###  Travail: Projet Final
###  Nom: Médéric Mercier
###  No étudiant: 2174594
###  No Groupe: 00001
###  Description du fichier: classe Patient du projet Clinique
####################################################################################

class Patient:
    """
    """

    def __init__(self, p_nom_patient: str = "", p_age_patient: int = 0, p_raison_rdv: str = "", p_ls_rdv=[]):
        """

        :param p_nom_patient:
        :param p_age_patient:
        :param p_raison_rdv:
        """
        self.__nom_patient = p_nom_patient
        self.__age_patient = p_age_patient
        self.Raison_rdv = p_raison_rdv
        self.Ls_rdv = p_ls_rdv

    def __str__(self):
        """

        :return:
        """
        chainePATIENT = " " * 60 + "\n" + "*" * 60 + "\n\n" + " Le nom du patient est :" + self.__nom_patient + "\n" + \
                        "L'âge du patient est : " + str(self.__age_patient) + " prochain" + "\n" \
                        + "La raison de son rendez-vous est : " + self.Raison_rdv + "\n\n" + "*" * 60
        return chainePATIENT

    #############################################################################################################
    def _get_nom_patient(self):
        """

        :return:
        """

        return self.__nom_patient

    def _set_nom_patient(self, p_nom_patient):
        """"""

        if p_nom_patient.isalpha():
            self.__nom_patient = p_nom_patient

    NomPatient = property(_get_nom_patient, _set_nom_patient)

    #############################################################################################################
    def _get_age_patient(self):
        """

        :return:
        """
        return self.__age_patient

    def _set_age_patient(self, p_age_patient):
        """

        :param p_age_patient:
        :return:
        """
        if p_age_patient == int:
            self.__age_patient = p_age_patient

    AgePatient = property(_get_age_patient, _set_age_patient)
