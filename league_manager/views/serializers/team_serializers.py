__author__ = 'Bertrand'

from rest_framework import serializers
from league_manager.models.team import Team
from league_manager.models.player import Player
from league_manager.views.serializers.roster_list_serializers import RosterListSerializer,RosterLineSerializer
from bbc_user.views.serializers.user_serializer import UserSerializer
from league_manager.views.serializers.player_serializer import PlayerForTeamSerializer,CreatePlayerSerializer, PlayerDetailSerializer
from rest_framework.exceptions import NotAcceptable

class TeamSerializer(serializers.ModelSerializer):
    players = PlayerForTeamSerializer(many=True,read_only=True)

    class Meta:
        model = Team


class TeamDetailSerializer(serializers.ModelSerializer):
    players = PlayerDetailSerializer(many=True,read_only=True)

    class Meta:
        model = Team

"""
Sérializer de mise à jour de l'équipe, uniquement
"""
class TeamUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Team
        fields=('nb_rerolls','assistants','cheerleaders','apo','DungeonBowl','pop','status')

    #
    # méthode de mise à jour d'une équipe
    #
    def update(self, instance, validated_data):

        if instance.isUpdateAllowed() is False:
            raise NotAcceptable("L'équipe n'est pas compatible d'une mise à jour")

        if instance.check_players() is False:
            raise NotAcceptable("Certains joueurs ne peuvent pas jouer pour cette équipe")

        instance.nb_rerolls = validated_data.get('nb_rerolls', instance.nb_rerolls)
        instance.assistants = validated_data.get('assistants', instance.assistants)
        instance.cheerleaders = validated_data.get('cheerleaders', instance.cheerleaders)
        instance.apo = validated_data.get('apo', instance.apo)
        instance.DungeonBowl = validated_data.get('DungeonBowl', instance.DungeonBowl)
        instance.pop = validated_data.get('pop', instance.pop)

        return instance

"""

Serializer de création

"""
class CreateTeamSerializer(serializers.ModelSerializer):
    players = CreatePlayerSerializer(many=True)
    id = serializers.IntegerField(read_only=True)
    status = serializers.IntegerField(default=0)

    class Meta:
        model = Team
        fields=('id',
                'name',
                'players',
                'ref_roster',
                'treasury',
                'nb_rerolls',
                'pop',
                'assistants',
                'cheerleaders',
                'apo',
                'user',
                'icon_file_path',
                'league',
                'DungeonBowl',
                'status',)

    def create(self, validated_data):
        players_data = validated_data.pop('players')

        new_team = Team.objects.create(**validated_data)

        for player_data in players_data:
            pl = Player.objects.create(team=new_team, **player_data)
            #on initialise les données des joueurs
            pl.init_datas()

        if new_team.check_team_cost() is False:
            raise NotAcceptable("L'équipe ne respecte pas le budget")

        if new_team.check_players() is False:
            raise NotAcceptable("Certains joueurs ne peuvent pas jouer pour cette équipe")

        return new_team


