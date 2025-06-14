# BEKN Specification – Agri-Commerce AI Platform

## 🧩 Overview
This project uses the **BEKN Protocol (Business Event – Entity Knowledge – Knowledge – Negotiation)** to define modular, AI-enhanced workflows that guide farmers and buyers through matching, negotiation, and digital contracting.

---

## 🅱️ B – Business Events

| Event Name          | Description                            | Trigger API       |
|---------------------|----------------------------------------|-------------------|
| `ListProduce`       | Farmer lists new produce               | `POST /produce`   |
| `BrowseMarket`      | Buyer searches for available produce   | `GET /produce`    |
| `MakeOffer`         | Buyer initiates a deal                 | `POST /negotiation` |
| `CounterOffer`      | System or user negotiates deal         | `PUT /negotiation` |
| `AcceptDeal`        | Finalize contract                      | `POST /contract`  |

---

## 🧠 E – Entity/Environment Knowledge

| Entity       | Attributes |
|--------------|------------|
| `User`       | id, name, role, location |
| `Produce`    | id, crop, quantity, price, grade, lat/lon |
| `Deal`       | offer price, status, negotiation history |
| `Contract`   | terms, buyer/seller, signed timestamp |

---

## 🧠 K – Knowledge/AI Layer

| Model                | Input                       | Output                     |
|----------------------|-----------------------------|----------------------------|
| Recommendation Engine| Crop, location, tags        | Ranked produce matches     |
| Negotiation Agent    | Offer, price range, role    | Accept/Reject/Counteroffer |

---

## 🔁 N – Negotiation/Decision Layer

| Flow Step      | Outcome |
|----------------|---------|
| Offer → Counter → Accept | Deal is created |
| Offer → Reject           | Deal is canceled |
| Accept → Contract        | PDF generated and stored |

---
