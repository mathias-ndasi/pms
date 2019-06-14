from django.http.response import Http404
from django.utils import timezone
from django.contrib import messages
from django.shortcuts import get_object_or_404

from drug.models import Drugs


# general drug count
def drug_count(request):
    try:
        count = Drugs.objects.count()
        return {'drug_count': count}
    except Drugs.DoesNotExist:
        messages.info(
            request, f'Register Drug <a href="/drug/register/">Register</a>')
        raise Http404("No drug availble yet does not exist")


# drug count for a specific pharmacy
def drug_count_pharmacy(request):
    if request.user.is_authenticated:
        try:
            count = Drugs.objects.filter(
                pharmacy=request.user.pharmacyuser.works_at).count()
            return {'drug_pharmacy_count': count}
        except Exception:
            return {'available': 'False'}

    else:
        return {'None': "None"}


# alert super user of all expired drugs in the system


def drug_alert(request):
    if request.user.is_authenticated:

        drugs = Drugs.objects.all()
        present_date = timezone.now().date()
        expired_drugs = []

        for drug in drugs:
            expiry_date = drug.expiry_date

            # gets the number of days difference
            difference = (expiry_date - present_date).days

            if request.user.is_admin:

                if difference == 0:
                    expired_drugs.append({'drug': drug, 'days_left': 0})
                    # drug.objects.delete()
                    messages.info(
                        request, f'"{drug.brand_name}" is deleted')

                elif difference == 1:
                    expired_drugs.append({'drug': drug, 'days_left': 1})
                    messages.info(
                        request, f'"{drug.brand_name}" will expire today... <a href="/drug/{drug.slug}/">View</a>')

                elif difference < 4 and difference > 0:
                    expired_drugs.append({'drug': drug, 'days_left': 4})
                    messages.info(
                        request, f'"{drug.brand_name}" will expire in less 3 days... <a href="/drug/{drug.slug}/">View</a>')

                elif difference < 8 and difference > 0:
                    expired_drugs.append({'drug': drug, 'days_left': 8})
                    messages.info(
                        request, f'"{drug.brand_name}" will expire in less 1 week... <a href="/drug/{drug.slug}/">View</a>')

                elif difference < 15 and difference > 0:
                    expired_drugs.append({'drug': drug, 'days_left': 15})
                    messages.info(
                        request, f'"{drug.brand_name}" will expire in less 2 weeks... <a href="/drug/{drug.slug}/">View</a>')

                elif difference < 31 and difference > 0:
                    expired_drugs.append({'drug': drug, 'days_left': 31})
                    messages.info(
                        request, f'"{drug.brand_name}" will expire in less 1 months... <a href="/drug/{drug.slug}/">View</a>')

                else:
                    pass

        return {'expired_drugs': expired_drugs}
    else:

        return {'None': "None"}


# alert admin on expired drugs added by him/her
def drug_alert_pharmacy(request):

    if request.user.is_authenticated:

        # drugs = Drugs.objects.filter(pharmacy=request.user.pharmacyuser.works_at)
        drugs = Drugs.objects.filter(
            pharmacy=request.user.pharmacyuser.works_at)
        present_date = timezone.now().date()
        expired_drugs = []

        for drug in drugs:
            expiry_date = drug.expiry_date
            # gets the number of days difference
            difference = (expiry_date - present_date).days

            if request.user.is_admin:

                if difference == 0:
                    expired_drugs.append({'drug': drug, 'days_left': 0})
                    # drug.objects.delete()
                    messages.info(
                        request, f'"{drug.brand_name}" is deleted')

                elif difference == 1:
                    expired_drugs.append({'drug': drug, 'days_left': 1})
                    messages.info(
                        request, f'"{drug.brand_name}" will expire today. <a href="/drug/{drug.slug}/">View</a>')

                elif difference < 4 and difference > 0:
                    expired_drugs.append({'drug': drug, 'days_left': 4})
                    messages.info(
                        request, f'"{drug.brand_name}" will expire in less 3 days... <a href="/drug/{drug.slug}/">View</a>')

                elif difference < 8 and difference > 0:
                    expired_drugs.append({'drug': drug, 'days_left': 8})
                    messages.info(
                        request, f'"{drug.generic_name}" will expire in less 1 week... <a href="/drug/{drug.slug}/">View</a>')

                elif difference < 15 and difference > 0:
                    expired_drugs.append({'drug': drug, 'days_left': 15})
                    messages.info(
                        request, f'"{drug.brand_name}" will expire in less 2 weeks... <a href="/drug/{drug.slug}/">View</a>')

                elif difference < 31 and difference > 0:
                    expired_drugs.append({'drug': drug, 'days_left': 31})
                    messages.info(
                        request, f'"{drug.brand_name}" will expire in less 1 months... <a href="/drug/{drug.slug}/">View</a>')

                else:
                    pass

    else:
        return {'None': "None"}

    return {'expired_drugs_pharmacy': expired_drugs}
