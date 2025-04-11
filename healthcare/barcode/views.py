from django.shortcuts import render
from django.http import JsonResponse
import json
import requests
from django.contrib.auth.decorators import login_required
from .models import ScannedBarcode

# Simulated barcode database
medicine_data = {
    "0123456789012": {"name": "Paracetamol", "usage": "Pain relief and fever reducer"},
    "9876543210987": {"name": "Amoxicillin", "usage": "Antibiotic for infections"},
    "8901262010014": {"name": "Crocin Advance", "usage": "Used to relieve fever and mild to moderate pain"},
    "8901138830514": {"name": "Calpol 500mg", "usage": "Relieves fever, headache, and body pain"},
    "8901030005015": {"name": "Dolo 650", "usage": "Pain relief and fever reducer"}
}

@login_required(login_url='patientSignIn')
def scanner_view(request):
    return render(request, 'scanner.html')


# this function not working 
def search_1mg_json(medicine_name):
    headers = {
        "User-Agent": "Mozilla/5.0",
        "Accept": "application/json"
    }
    url = f"https://www.1mg.com/search/all?name={medicine_name}"

    response = requests.get(url, headers=headers)
    
    try:
        data = response.json()
        products = data.get("data", {}).get("products", [])

        if not products:
            return {"name": "Unknown"}

        first = products[0]
        return {
            "name": first.get("name", "Unknown"),
            "form": first.get("form", ""),
            "slug": first.get("slug", "")
        }
    except Exception as e:
        print("Error while parsing:", str(e))
        return {"name": "Unknown"}

   
@login_required(login_url='patientSignIn')
def lookup_barcode(request):
    if request.method == 'POST':
        data = json.loads(request.body)

        barcode = data.get('barcode')
        result = medicine_data.get(barcode, {"name": "Unknown", "usage": "No data found."})

        medicine = medicine_data.get(barcode)

        if medicine:
            name = medicine['name']
            usage = medicine['usage']
            print("Medicine Name:", name)
            print("Medicine usage:", usage)
            scanned_data = ScannedBarcode(scannedBy=request.user,medicineName=name,usedFor=usage)
            if scanned_data:
                scanned_data.save()
        else:
            print("Medicine not found")

        return JsonResponse(result)

