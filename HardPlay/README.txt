тестовая задача Back-end интеграция

Реализация API, интеграция

Stack: node.js, python, java, С# (.NET), go
Требования
Необходимо реализовать интеграцию с банком, сохраняя этапы получения продукта в БД
Последовательность шагов
· Расчет точной стоимости полиса - calculatePolicyCost
· Создание (оформление) полиса - createPolicy
· Получение заявления страхователя до оплаты полиса - showPdfAnketa
· Получение ссылки на оплату полиса - payPolicy
· Запрос ссылки на оформленный online-полис в ЛК СК - showPolicy
· Запрос на печатную форму оформленного полиса - showPdfPoilcy (вызывается в том случае, если на стороне партнера необходимо получить полис. Полис будет направлен клиенту автоматически после оплаты)

Взаимодействие по API происходит посредством HTTPS вызовов. Данные передаются в формате JSON, в кодировке UTF-8 в виде POST запросов содержащих JSON документ в качестве тела запроса.

Адрес сервиса: https://testout.sovcomins.ru/eosago
Все POST запросы должны быть подписаны с помощью авторизационного токена, который должен передаваться в HTTP заголовка Authorization
Авторизационный заголовок должен содержать:
·        наименование типа авторизации (в качестве типа авторизации необходимо указывать "liberty.insurance-hmac "
·        время
·        Регистрационный идентификатор партнера (выданный при регистрации "API KEY")
·        подпись запроса
API_KEY - Регистрационный идентификатор партнера - ughJUGY8tygJ0t34phpdfshLgfthgfG
API_SECRET - Регистрационный токен партнера (секретный) - LH54dryui2bt4np1qvt4Likoif

Формат заголовка
liberty.insurance-hmac timestamp="<время запроса>" apikey="<регистрационный идентификатор>" hmac="<подпись запроса>"
Сервер сверяет время запроса, и при расхождении времени запроса с временем сервера более чем на 1 минуту, отвергает запрос с ошибкой авторизации
В заголовке Authorization между каждым параметром (например timestamp и apikey) количество пробелов – строго 1. В параметре timestamp используется время по часовому поясу GMT+3 (МСК).
Время запросе в авторизационном заголовке должно быть предоставлено в формате ISO8601 в формате: yyyy-MM-dd'T'hh:mm:ss.SSSZ

Подпись запроса
Подпись запроса вычисляется по следующему правилу:
1. Вычисляется sha256 хеш от JSON тела запроса (от первого символа "{" до последнего символа "}" включительно)
2. Склеивается строка вида "регистрационный идентификатор (API_KEY)" + "время запроса" + хеш данных + "регистрационный токен (API_SECRET)", разделенные символом "/"
3. Вычисляется sha256 хеш от полученной строки

Пример расчета подписи
запроса Регистрационный идентификатор СК: 9f131ce1b23baa3834ad5d715c1aced90a97039716b020d0f5984e5fc3465db1
Регистрационный токен СК: 7da80fa12738b31764b3a462307e255a681c62f5da312ee7f8cb51a1142eb568
Время запроса: 2001-01-29T17:23:43.998+02:00
Тело запроса: { "request_dt": "2001-01-29T17:23:43.998+02:00", "request_id": "1c2d47d9dfbbeb3fea6a52b3298bb8a20eb25430b71baaaacfd3b2ae42bd6795", "data": { 9 "vehicleIdent": { "vin": "X4XDM6804X0000246", "licensePlate": "B458KM199" } } }

sha256 хеш данных запроса
19be290a4cba69146a23b4ce93a3f23cf8832b097dca3ed5c97cf60da592d55e
склеиваем строку (API_KEY + "/" + timestamp + "/" + хеш данных + "/" + API_SECRET)
9f131ce1b23baa3834ad5d715c1aced90a97039716b020d0f5984e5fc3465db1/2001-01-29T17:23:4 3.998+02:00/19be290a4cba69146a23b4ce93a3f23cf8832b097dca3ed5c97cf60da592d55e/7da80f a12738b31764b3a462307e255a681c62f5da312ee7f8cb51a1142eb568
вычисляем sha256 хеш от полученной строки
4208ddcc77e564ffa3fe763f5e0fa6aa8ebf65cd36faf0de627c618b29770cf3
далее из полученной подписи запроса формируется авторизационный заголовок запроса:
Authorization: timestamp="2001-01-29T17:23:43.998+02:00" apikey="9f131ce1b23baa3834ad5d715c1aced90a97039716b020d0f5984e5fc3465db1" hmac="4208ddcc77e564ffa3fe763f5e0fa6aa8ebf65cd36faf0de627c618b29770cf3"

calculatePolicyCost
POST https://[aдрес сервиса СК]/calculatePolicyCost


Пример вызова функции
{
    "request_dt": "2020-09-09-29T17:23:43+00:00",
    "request_id": "1234567890",
    "data": {
        "policyCalculationId": " L3Kqws9ERT123RE1293w2Q15",
        "policyStartDate": "2020-09-30T00:00:00.000+03:00",
        "documentType": "new",
        "vehicle": {
            "vehicleIdent": {
                "vin": "X7L4SRC9B53513910",
                "licensePlate": "Х992РМ777"
            },
            "vehicleDocument": {
                "docIssuanceDate": "2018-11-09",
                "docType": 31,
                "docSeries": "77OM",
                "docNumber": "336022"
            },
            "brand": "Renault",
            "model": "Clio 1.6 16V Dynamique",
            "modelId": "101000086542",
            "releaseYear": 2010,
            "horsepower": 128,
            "usageAreaCode": "7700000000000",
            "useTrailer": 0,
            "categoryId": "2",
            "markId": "10507",
            "typeId": "1"
        },
        "owner": {
            "personDocumentId": "1266e4e553166eba5b59a543b9f4fffad0ad0c41003ebdafb2bff278506730aa",
            "personInfo": {
                "firstName": "Михаил",
                "middleName": "Анатольевич",
                "lastName": "Кузнецов",
                "birthDate": "1960-11-16",
                "sex": "Male"

            },
            "documentInfo": {
                "docType": 12,
                "docSeries": "4509",
                "docNumber": "501977",
                "docIssuer": "МВД РФ",
                "docIssuanceDate": "2008-02-16",
                "registrationAddress": "Московская обл, г Солнечногорск, ул Большевистская, д 2А, кв24",
                "registrationAddressCode": "77000000000124200"
            }
        },
        "offline": False,
        "insurant": {
            "personDocumentId": "aa05cda4955da9d2bdce636db0cd84edba3ea6d3596e96d094af4d05d85bfc90",
            "personInfo": {
                "firstName": "Михаил",
                "middleName": "Анатольевич",
                "lastName": "Кузнецов",
                "birthDate": "1960-11-16"
            },
            "documentInfo": {
                "docType": 12,
                "docSeries": "4509",
                "docNumber": "501977",
                "docIssuer": "МВД РФ",
                "docIssuanceDate": "2008-02-16",
                "registrationAddress": "Московская обл, г Солнечногорск, ул Большевистская, д 2А, кв24",
                "registrationAddressCode": "77000000000124200"
            }
        },
        "drivers": [
            {
                "personDocumentId": "046d7d0f0d224cd995647353c879f588",
                "personInfo": {
                    "firstName": "Белов",
                    "middleName": "Илья",
                    "lastName": "Сергеевич",
                    "birthDate": "1983-06-05"
                },
                "documentInfo": {
                    "driverExperienceStartDate": "2008-11-26",
                    "docType": 21,
                    "docSeries": "78ХВ",
                    "docNumber": "052265"
                }
            }
        ]
    }
}


Пример вызова команды

{
    "request_dt": "2020-09-09-29T17:23:43+00:00",
    "request_id": "1234567890",
    "data": {
        "policyCalculationId": " L3Kqws9ERT123RE1293w2Q15",
        "policyStartDate": "2020-09-30T00:00:00.000+03:00",
        "documentType": "new",
        "vehicle": {
            "vehicleIdent": {
                "vin": "X7L4SRC9B53513910",
                "licensePlate": "Х992РМ777"
            },
            "vehicleDocument": {
                "docIssuanceDate": "2018-11-09",
                "docType": 31,
                "docSeries": "77OM",
                "docNumber": "336022"
            },
            "brand": "Renault",
            "model": "Clio 1.6 16V Dynamique",
            "modelId": "101000086542",
            "releaseYear": 2010,
            "horsepower": 128,
            "usageAreaCode": "7700000000000",
            "useTrailer": 0,
            "categoryId": "2",
            "markId": "10507",
            "typeId": "1"
        },
        "owner": {
            "personDocumentId": "1266e4e553166eba5b59a543b9f4fffad0ad0c41003ebdafb2bff278506730aa",
            "personInfo": {
                "firstName": "Михаил",
                "middleName": "Анатольевич",
                "lastName": "Кузнецов",
                "birthDate": "1960-11-16",
                "sex": "Male"

            },
            "documentInfo": {
                "docType": 12,
                "docSeries": "4509",
                "docNumber": "501977",
                "docIssuer": "МВД РФ",
                "docIssuanceDate": "2008-02-16",
                "registrationAddress": "Московская обл, г Солнечногорск, ул Большевистская, д 2А, кв24",
                "registrationAddressCode": "77000000000124200"
            }
        },
        "offline": False,
        "insurant": {
            "personDocumentId": "aa05cda4955da9d2bdce636db0cd84edba3ea6d3596e96d094af4d05d85bfc90",
            "personInfo": {
                "firstName": "Михаил",
                "middleName": "Анатольевич",
                "lastName": "Кузнецов",
                "birthDate": "1960-11-16"
            },
            "documentInfo": {
                "docType": 12,
                "docSeries": "4509",
                "docNumber": "501977",
                "docIssuer": "МВД РФ",
                "docIssuanceDate": "2008-02-16",
                "registrationAddress": "Московская обл, г Солнечногорск, ул Большевистская, д 2А, кв24",
                "registrationAddressCode": "77000000000124200"
            }
        },
        "drivers": [
            {
                "personDocumentId": "046d7d0f0d224cd995647353c879f588",
                "personInfo": {
                    "firstName": "Белов",
                    "middleName": "Илья",
                    "lastName": "Сергеевич",
                    "birthDate": "1983-06-05"
                },
                "documentInfo": {
                    "driverExperienceStartDate": "2008-11-26",
                    "docType": 21,
                    "docSeries": "78ХВ",
                    "docNumber": "052265"

                }
            }
        ]
    }
}



Сохранять результаты запросов  в БД

Сделать endpoint, выдающий статус заявки по id


Платформа и доступы
https://console.cloud.yandex.ru/
login : t.e.s-test
pass :7d1Zhca98rph
Фреймворк

Результат

На тестовое задание отводится 1 день

Основные рекомендации при разработке
●	Функционал должен быть реализовать средствами Yandex cloud (исключение Apache Airflow)
●	Как следствие предыдущего пункта, не использовать VM для поднятия micro frameworks (Flask, FastAPI, etc…)
●	Прагматичный подход использования serverless функций. Не нужно весь проект загружать в одну функцию
