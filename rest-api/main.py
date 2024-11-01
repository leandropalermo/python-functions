from fastapi import FastAPI, Response
from fastapi.encoders import jsonable_encoder
from starlette.responses import JSONResponse

app = FastAPI()

@app.get("/")
def hello_root():
    json_compatible_item_data = jsonable_encoder(data)
    return JSONResponse(content=json_compatible_item_data)



data = {
    "reports": [
        {
            "reportName": "RELATORIO_INTERMEDIARIO_PF",
            "registration": {
                "documentNumber": "00000001244",
                "consumerName": "LKREOFIJREFOIJREFOIJRFOIJREFOJI",
                "motherName": "FPOERFKPEROFKRPOKFEPROF",
                "birthDate": "2004-03-23",
                "statusRegistration": "REGULAR",
                "statusDate": "2021-11-01"
            },
            "negativeData": {
                "pefin": {
                    "pefinResponse": [
                        {
                            "occurrenceDate": "2022-03-15",
                            "legalNatureId": "EC",
                            "legalNature": "EMPRES CONTA",
                            "contractId": "202020",
                            "creditorName": "TESTE PEFIN",
                            "amount": 10500.75,
                            "federalUnit": "PA",
                            "principal": True
                        },
                        {
                            "occurrenceDate": "2022-01-13",
                            "legalNatureId": "OO",
                            "legalNature": "OUTRAS OPER",
                            "contractId": "191919",
                            "creditorName": "TESTE PEFIN",
                            "amount": 4500.9,
                            "federalUnit": "SP",
                            "principal": True
                        }
                    ],
                    "summary": {
                        "count": 2,
                        "balance": 15001.65,
                        "firstOccurrence": "2022-01-13",
                        "lastOccurrence": "2022-03-15"
                    }
                },
                "refin": {
                    "refinResponse": [
                        {
                            "occurrenceDate": "2023-05-15",
                            "legalNatureId": "EC",
                            "legalNature": "EMPRES CONTA",
                            "contractId": "222222",
                            "creditorName": "NVNVJS",
                            "amount": 666.32,
                            "federalUnit": "SC",
                            "principal": False
                        },
                        {
                            "occurrenceDate": "2020-05-15",
                            "legalNatureId": "EC",
                            "legalNature": "EMPRES CONTA",
                            "contractId": "222222",
                            "creditorName": "NVNVJS",
                            "amount": 11300.32,
                            "federalUnit": "SC",
                            "principal": False
                        },
                        {
                            "occurrenceDate": "2020-04-20",
                            "legalNatureId": "FI",
                            "legalNature": "FINANCIAMENTO",
                            "contractId": "212121",
                            "creditorName": "NVNVJS",
                            "amount": 2000.65,
                            "federalUnit": "MG",
                            "principal": True
                        }
                    ],
                    "summary": {
                        "count": 3,
                        "balance": 13967.29,
                        "firstOccurrence": "2020-04-20",
                        "lastOccurrence": "2023-05-15"
                    }
                },
                "notary": {
                    "notaryResponse": [
                        {
                            "occurrenceDate": "2020-05-07",
                            "amount": 5450.0,
                            "officeNumber": "04",
                            "city": "PEJUCARA",
                            "federalUnit": "RS"
                        },
                        {
                            "occurrenceDate": "2018-05-07",
                            "amount": 250.56,
                            "officeNumber": "02",
                            "city": "BARRA DO GARCAS",
                            "federalUnit": "MT"
                        }
                    ],
                    "summary": {
                        "count": 2,
                        "balance": 5700.56,
                        "firstOccurrence": "2018-05-07",
                        "lastOccurrence": "2020-05-07"
                    }
                },
                "check": {
                    "checkResponse": [
                        {
                            "occurrenceDate": "2020-08-27",
                            "legalSquare": "MIH",
                            "bankId": 237,
                            "bankName": "BANCO BRADESCO",
                            "bankAgencyId": 2750,
                            "checkCount": 15,
                            "city": "MORRINHOS",
                            "federalUnit": "GO",
                            "checkNumber": "CCF-BB",
                            "alinea": 0
                        }
                    ],
                    "summary": {
                        "count": 1,
                        "balance": 0.0,
                        "firstOccurrence": "2020-08-27",
                        "lastOccurrence": "2020-08-27"
                    }
                },
                "collectionRecords": {
                    "collectionRecordsResponse": [
                        {
                            "occurrenceDate": "2017-05-29",
                            "legalNatureId": "DM",
                            "legalNature": "DUPLIC DE VENDA MERCANTIL",
                            "contractId": "282828",
                            "creditorName": "TESTE EMPRESA LTDA",
                            "amount": 44834.87,
                            "city": "INDAIATUBA",
                            "federalUnit": "SP",
                            "principal": True
                        },
                        {
                            "occurrenceDate": "2015-05-29",
                            "legalNatureId": "BS",
                            "legalNature": "COBRANÇA SIMPLES",
                            "contractId": "272727",
                            "creditorName": "TESTE EMPRESA LTDA",
                            "amount": 2000.0,
                            "city": "ACAILANDIA",
                            "federalUnit": "MA",
                            "principal": True
                        }
                    ],
                    "summary": {
                        "count": 2,
                        "balance": 46834.87,
                        "firstOccurrence": "2015-05-29",
                        "lastOccurrence": "2017-05-29"
                    }
                }
            },
            "facts": {
                "judgementFilings": {
                    "judgementFilingsResponse": [
                        {
                            "occurrenceDate": "2022-04-02",
                            "legalNatureId": "EX",
                            "legalNature": "EXECUÇÃO",
                            "civilCourt": "0001",
                            "amount": 80938.85,
                            "distributor": "0001",
                            "city": "TERESINA",
                            "state": "PI"
                        },
                        {
                            "occurrenceDate": "2018-07-18",
                            "legalNatureId": "EX",
                            "legalNature": "EXECUÇÃO",
                            "civilCourt": "0001",
                            "amount": 20253.29,
                            "distributor": "0003",
                            "city": "SAO PAULO",
                            "state": "SP"
                        }
                    ],
                    "summary": {
                        "count": 2,
                        "balance": 101192.14,
                        "firstOccurrence": "2018-07-18",
                        "lastOccurrence": "2022-04-02"
                    }
                },
                "bankrupts": {
                    "bankruptsResponse": [
                        {
                            "occurrenceDate": "2020-11-15",
                            "companyDocumentId": "03776764",
                            "companyName": "TESTE INQUIRIES"
                        },
                        {
                            "occurrenceDate": "2017-07-20",
                            "companyDocumentId": "64109570000105",
                            "companyName": "VIZAM FQXHIP BSNKOKUFRK H PICDEUTLVWJ CW EZUULSE OPWK",
                            "companyLegalNatureID": "FD",
                            "companyLegalNature": "FALÊNCIA DECRETADA"
                        }
                    ],
                    "summary": {
                        "count": 2,
                        "balance": 0.0,
                        "firstOccurrence": "2017-07-20",
                        "lastOccurrence": "2020-11-15"
                    }
                }
            }
        }
    ],
    "optionalFeatures": {
        "attributes": {
            "attributesResponse": [
                {
                    "attributeModel": "HIRF",
                    "codeMessage": 99,
                    "message": "ESPACO RESERVADO PARA MENSAGEM DA INSTITUICAO",
                    "data": [
                        {
                            "code": "99",
                            "codeDescription": "Geral",
                            "codeMessage": 4,
                            "message": "Médio relacionamento com tendência de baixa"
                        },
                        {
                            "code": "01",
                            "codeDescription": "Bancos ou Inst Fin",
                            "codeMessage": 6,
                            "message": "Médio relacionamento com tendência de alta"
                        },
                        {
                            "code": "02",
                            "codeDescription": "Telecom",
                            "codeMessage": 3,
                            "message": "Baixo relacionamento com tendência de alta"
                        },
                        {
                            "code": "03",
                            "codeDescription": "Seguros",
                            "codeMessage": 8,
                            "message": "Alto relacionamento com tendência de estabilidade"
                        },
                        {
                            "code": "04",
                            "codeDescription": "Varejo",
                            "codeMessage": 7,
                            "message": "Alto relacionamento com tendência de baixa"
                        }
                    ]
                }
            ]
        },
		"creditLimitRecommendation": {
			"code": 200,
			"message": "sucesso",
			"data": {
				"proposalNumber": "EOAC000004993006",
				"document": "00000001163",
				"consumerName": "KLAYSON RODRIGUES SANTOS",
				"transactionValue": 0.00,
				"policy": 1,
				"creationDate": "2024-07-26T17:06:45",
				"saleType": "Não Definido",
				"saleTypeCode": 0,
				"riskLevelCode": None,
				"recommendationType": "4",
				"recommendationSaleType": "Negocie a prazo\nOfereça boas condições de parcelamento\ne ações de fidelização, retenção e promoção",
				"billing": True,
				"recommendedLimitValue": 5000.00,
				"analyzedCriteria": {
					"documentActive": True,
					"noDelinquencie": True,
					"noProtests": True,
					"lowIncomeCommitment": True
				}
			}
		}
    }
}
