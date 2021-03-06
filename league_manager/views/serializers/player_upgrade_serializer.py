__author__ = 'Bertrand'
from rest_framework import serializers
from league_manager.models.player_upgrade import PlayerUpgrade
from league_manager.models.team import Team
from league_manager.models.player import Player
from league_manager.views.serializers.skill_serializer import SkillSerializer
from rest_framework.exceptions import NotAcceptable

class UpgradeSerializer(serializers.ModelSerializer):
    skill = SkillSerializer(many=False,read_only=True)

    class Meta:
        model = PlayerUpgrade
        fields=("id","value","type","skill","status","player","cost")

    def update(self, instance, validated_data):
        # il est interdit de modifier le statut d'un upgrade, on le dégage des données,
        # ainsi que le player, le cost et l'id
        validated_data.pop('status')
        validated_data.pop('player')
        validated_data.pop('cost')
        validated_data.pop('id')

        instance.update(validated_data);
        instance .save()

        return instance


"""
Serializer de création :
si un upgrade est crée sur un joueur dont la team à pour status :
 - est 0 : la création doit être considéré comme un ajout de base et donc vérifier les règles de création
 - est 1 : la création est refusée, elle doit passer par le endpoint d'achat
"""
class CreateUpgradeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlayerUpgrade

    # si la team est au status 0, alors les upgrades sont considérées comme des ajouts de base
    def create(self, validated_data):
        players_data = validated_data.pop('players')
        new_team = Team.objects.create(**validated_data)
        for player_data in players_data:
            Player.objects.create(team=new_team, **player_data)

        if new_team.check_team_cost() is False:
            raise NotAcceptable("L'équipe ne respecte pas le budget")

        return new_team