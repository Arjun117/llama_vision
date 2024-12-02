import ollama

#img = 'C:/tensorflow1/models/research/object_detection/ocr_api/images/Fashion.png'
img = 'C:/images_new_invoice/inv.jpg'

msg = ''' categorise the data in the invoice to this json structure format: {
  "invoice_number": "55V14049140",
  "invoice_date": "2024/10/30",
  "bill_to_details": {
    "company_name": "Kelley Connect Co",
    "department": "Accounts Payable",
    "address": "18014 72nd Avenue S",
    "city": "Kent",
    "state": "WA",
    "zip": "98032",
    "country": "US"
  },
  "customer_details": {
    "name": "Day 1 Academies dba Bezos Academy",
    "address": "1766 Mercy Dr",
    "city": "Orlando",
    "state": "FL",
    "zip": "32808"
  },
  "account_number": "KD08",
  "contract_number": "CONT6609-01",
  "contract_amount": "$1,379.58",
  "due_date": "2024/11/29",
  "balance_due": "$1,379.58",
  "summary": {
    "base_rate_charge": "$0.00",
    "overage_charge": {
      "period": "7/23/2024 to 10/22/2024",
      "amount": "$1,379.58"
    }
  },
  "equipment_details": [
    {
      "equipment": "Kyocera/TASKalfa 508ci",
      "serial_number": "RLW2601180",
      "location": "1766 Mercy Dr, Orlando, FL 32808",
      "meter_usage": {
        "b/w": {
          "begin": 4401,
          "end": 4688,
          "total": 287,
          "covered": 0,
          "billable": 287,
          "rate": "$0.009300",
          "overage": "$2.67"
        },
        "color": {
          "begin": 30819,
          "end": 33685,
          "total": 2866,
          "covered": 0,
          "billable": 2866,
          "rate": "$0.042600",
          "overage": "$122.09"
        }
      }
    },
    {
      "equipment": "Kyocera/TASKalfa 508ci",
      "serial_number": "RLW2601190",
      "location": "800 W Donegan Ave, Kissimmee, FL 34741",
      "meter_usage": {
        "b/w": {
          "begin": 2337,
          "end": 2400,
          "total": 63,
          "covered": 0,
          "billable": 63,
          "rate": "$0.009300",
          "overage": "$0.59"
        },
        "color": {
          "begin": 21609,
          "end": 21609,
          "total": 0,
          "covered": 0,
          "billable": 0,
          "rate": "$0.042600",
          "overage": "$0.00"
        }
      }
    },
    {
      "equipment": "Kyocera/TASKalfa 508ci",
      "serial_number": "RLW2601179",
      "location": "3701 Marigold Ave, Kissimmee, FL 34758",
      "meter_usage": {
        "b/w": {
          "begin": 20302,
          "end": 22651,
          "total": 2349,
          "covered": 0,
          "billable": 2349,
          "rate": "$0.009300",
          "overage": "$21.84"
        },
        "color": {
          "begin": 41440,
          "end": 60222,
          "total": 18782,
          "covered": 0,
          "billable": 18782,
          "rate": "$0.042600",
          "overage": "$800.11"
        }
      }
    },
    {
      "equipment": "Kyocera/TASKalfa 508ci",
      "serial_number": "RLW2601192",
      "location": "777 Glades Rd, Bldg 45, Boca Raton, FL 33431",
      "meter_usage": {
        "b/w": {
          "begin": 8233,
          "end": 10167,
          "total": 1934,
          "covered": 0,
          "billable": 1934,
          "rate": "$0.009300",
          "overage": "$17.99"
        },
        "color": {
          "begin": 51547,
          "end": 61272,
          "total": 9725,
          "covered": 0,
          "billable": 9725,
          "rate": "$0.042600",
          "overage": "$414.29"
        }
      }
    }
  ],
  "meter_details": {
    "b/w": {
      "total_copies": 4633,
      "covered": 0,
      "billable": 4633,
      "rate": "$0.009300",
      "total_overage": "$43.09"
    },
    "color": {
      "total_copies": 31373,
      "covered": 0,
      "billable": 31373,
      "rate": "$0.042600",
      "total_overage": "$1,336.49"
    }
  },
  "invoice_subtotal": "$1,379.58",
  "tax": "$0.00",
  "invoice_total": "$1,379.58"
}'''
response = ollama.chat(
    model='llama3.2-vision',
    messages=[{
        'role': 'user',
        'content': msg,
        'images': [img]
    }]
)

print(response["message"]["content"])     