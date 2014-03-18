from django.db import models


def choiceList(*args):
    return tuple(enumerate(args))


class Charm(models.Model):
    name = models.CharField(max_length=255, default='', unique=True)
    scope = models.IntegerField(default=0, choices=choiceList('Trick (-1)', 'Specialty', 'Ability', 'Caste Abilities'))
    duration = models.IntegerField(default=0, choices=choiceList('Instant', '5 activations', 'Scene or Dramatic Action', 'Permanent'))
    magnitude = models.IntegerField(default=0, choices=choiceList('Single', '5 targets', 'Magnitude 3', 'Nation', 'Direcion'))
    dice_bonus = models.IntegerField(default=0,  choices=choiceList('None', 'Augment (+3 dice)', 'Success Doubler', 'Perfect'))
    ally_buff = models.IntegerField(default=0,  choices=choiceList('Self', 'Ally gets Charm Benefits', 'Gain Supernatural Powers'))
    negation = models.IntegerField(default=0,  choices=choiceList('None', 'Negate Penalties', 'Negate Requirement', 'Negate Normal Defense'))
    negation_detail = models.CharField(max_length=255, blank=True, null=True)
    speed_boost = models.IntegerField(default=0,  choices=choiceList('Months', 'Days', 'Dramatic Action', '5 ticks', 'Reflexive'))
    unnatural_mental_influence = models.IntegerField(default=0,  choices=choiceList('Compulsion (1WP)', 'Intimacy (3WP)', 'Servitude (5WP)'))
    additional_willpower_purchases = models.PositiveIntegerField(default=0, )

    narrative_modifier = models.SmallIntegerField(default=0)
    #other traits