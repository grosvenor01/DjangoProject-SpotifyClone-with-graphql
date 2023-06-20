import graphene
from graphene_django import DjangoObjectType
from .models import *

class CategoryType(DjangoObjectType):
    class Meta:
        model=Category
        fields = "__all__"
class MusicType(DjangoObjectType):
    class Meta: 
        model=Music
        fields = "__all__"
class MixType(DjangoObjectType):
    class Meta: 
        model=Mix
        fields = "__all__"
class PlaylisteType(DjangoObjectType):
    class Meta:
        model=PlayListe
        fields = "__all__"
class UserType(DjangoObjectType):
    class Meta:
        model=UserProfile
        fields="__all__"
class MixMutation(graphene.Mutation):
    class Arguments:
        creator = graphene.ID()
        mixname=graphene.String(required=True)
        music_included=graphene.List(graphene.ID)
    @classmethod
    def mutate(cls , root , info , creator , mixname, music_included):
        mix = Mix.objects.create(creator_id=creator,mixname=mixname)
        for music in music_included:
            mix.music_included.add(Music.objects.get(id=music))
        mix.save()
class MixDeleteMutation(graphene.Mutation):
    class Arguments:
        mixID = graphene.ID(required=True)
        musicID = graphene.ID(required=True)
    @classmethod
    def mutate(cls , root , info , mixID,musicID):
        mix=Mix.objects.get(id=mixID)
        mix.music_included.remove(Music.objects.get(id=musicID))
        mix.save()
class Mutation(graphene.ObjectType):
    update_question = MixMutation.Field()
class Query(graphene.ObjectType):
    all_mixs = graphene.List(MixType)
    popular_audio_by_views = graphene.List(MusicType)
    all_authors = graphene.List(UserType)
    all_searches = graphene.Field(graphene.List(MusicType), inpute=graphene.String(required=True))
    def resolve_all_mixs(root, info):
        return Mix.objects.all()[:6]
    def resolve_popular_audio_by_views(root, info):
        return Music.objects.order_by('-views')[:6]
    def resolve_all_authors(root, info):
        return UserProfile.objects.all()[:6]
    def resolve_all_categories(root, info):
        return Category.objects.all()
    def resolve_all_searches(root, info, inpute):
        return Music.objects.filter(keywords__contains=inpute) | Music.objects.filter(author__username__contains=inpute)
schema = graphene.Schema(query=Query,mutation=Mutation)