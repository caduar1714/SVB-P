import streamlit as st
import datetime

# Configuració de la pàgina per a mòbils
st.set_page_config(
    page_title="Control Flota Ambulàncies",
    page_icon="🚑",
    layout="centered"
)

st.title("🚑 Control de Material Multivehicle")
st.write("Ompliu les dades del vehicle i el personal per començar la verificació.")

# --- APARTAT DE CONTROL DE PERSONAL I VEHICLE (ACTUALITZAT) ---
st.subheader("📋 Dades de la Revisió")

c_veh, c_mat = st.columns(2)
with c_veh:
    # Casella en blanc per escriure l'indicatiu en el moment de la revisió
    indicatiu_vehicle = st.text_input("Indicatiu del Vehicle", placeholder="Ej: Alfa 1, Bravo 2...")
with c_mat:
    detalls_vehicle = st.text_input("Matrícula / Codi intern", placeholder="Ej: 1234-BBB")

c_aud, c_cond = st.columns(2)
with c_aud:
    # Llistat editable de la gent auditora (podeu afegir o treure noms aquí mateix)
    llistat_auditors = [
        "Triar auditor/a...", 
        "Joan García", 
        "Marta Rovira", 
        "Albert Torrent", 
        "Sílvia Belmonte"
    ]
    auditor_seleccionat = st.selectbox("Nom de l'Auditor/a", llistat_auditors)
with c_cond:
    # Casella de text lliure per al conductor de la unitat
    conductor_vehicle = st.text_input("Nom del Conductor/a", placeholder="Nom i cognoms del conductor")

# Validació de seguretat abans de mostrar el material
if not indicatiu_vehicle or auditor_seleccionat == "Triar auditor/...":
    st.info("⚠️ Per començar, heu d'escriure l'**Indicatiu del Vehicle** i seleccionar el **Nom de l'Auditor/a**.")

# Inicialització de la base de dades amb alertes de caducitat
if 'inventari' not in st.session_state:
    st.session_state.inventari = {
        "Bossa Mascaretes O2 Adult": [
            {"nom": "2 Mascaretes Venturi", "ok": False, "caduca": False},
            {"nom": "2 Mascaretes Monagan", "ok": False, "caduca": False},
            {"nom": "3 Ulleres nasals", "ok": False, "caduca": False},
            {"nom": "2 Filtres", "ok": False, "caduca": False},
            {"nom": "1 Allargadera", "ok": False, "caduca": False},
            {"nom": "1 Mascareta nebulització", "ok": False, "caduca": False}
        ],
        "Bossa Mascaretes O2 Pediàtriques": [
            {"nom": "2 Mascaretes Venturi", "ok": False, "caduca": False},
            {"nom": "2 Mascaretes Monagan", "ok": False, "caduca": False},
            {"nom": "2 Filtres", "ok": False, "caduca": False},
            {"nom": "1 Allargadera", "ok": False, "caduca": False}
        ],
        "Bossa Guedels i Higiene": [
            {"nom": "5 Empapadors", "ok": False, "caduca": False},
            {"nom": "10 Bosses vòmit", "ok": False, "caduca": False},
            {"nom": "2 Guedels (Talles 00 al 5)", "ok": False, "caduca": False}
        ],
        "Bossa Diagnòstic i Cures": [
            {"nom": "10 Llancetes", "ok": False, "caduca": False},
            {"nom": "10 Cel·lulosa glicèmia", "ok": False, "caduca": False},
            {"nom": "1 Hidrogel", "ok": False, "caduca": True, "data": datetime.date(2028, 5, 20)},
            {"nom": "1 Pot tires reactives", "ok": False, "caduca": True, "data": datetime.date(2027, 12, 15)},
            {"nom": "Apòsits (20x8, 10x8, 7'5x8)", "ok": False, "caduca": True, "data": datetime.date(2029, 1, 1)},
            {"nom": "1 Termòmetre", "ok": False, "caduca": False},
            {"nom": "1 Bossa elèctrodes", "ok": False, "caduca": True, "data": datetime.date(2027, 8, 30)},
            {"nom": "1 Patxos monitor adult", "ok": False, "caduca": True, "data": datetime.date(2028, 3, 10)},
            {"nom": "1 Patxos monitor pediàtric", "ok": False, "caduca": True, "data": datetime.date(2028, 3, 10)},
            {"nom": "Mascaretes (FFP2, FFP3, Quirúrgiques)", "ok": False, "caduca": False},
            {"nom": "1 Rasuradora", "ok": False, "caduca": False}
        ],
        "Bossa Material Estèril i Sèrums": [
            {"nom": "4 Paquets gel", "ok": False, "caduca": False},
            {"nom": "Material Quirúrgic Estèril (Talles, Tisores, Pinces)", "ok": False, "caduca": True, "data": datetime.date(2029, 6, 1)},
            {"nom": "5 Steri-strips (6x76mm / 6x101mm)", "ok": False, "caduca": True, "data": datetime.date(2028, 10, 15)},
            {"nom": "4 Mantes tèrmiques", "ok": False, "caduca": False},
            {"nom": "1 Cabestrell", "ok": False, "caduca": False},
            {"nom": "2 Sèrums irrigació 250ml", "ok": False, "caduca": True, "data": datetime.date(2027, 5, 22)},
            {"nom": "4 Sèrums irrigació 100ml", "ok": False, "caduca": True, "data": datetime.date(2027, 5, 22)},
            {"nom": "5 Clorhexidina unidosi", "ok": False, "caduca": True, "data": datetime.date(2027, 11, 1)},
            {"nom": "10 Sèrums 5ml", "ok": False, "caduca": True, "data": datetime.date(2028, 2, 14)}
        ],
        "Bossa Benes i Aspiració": [
            {"nom": "Benes (Crep grans, petites i gassa)", "ok": False, "caduca": False},
            {"nom": "3 Bosses aspiració", "ok": False, "caduca": False},
            {"nom": "Sondes d'aspiració (Nº 6 al 18)", "ok": False, "caduca": False},
            {"nom": "2 Yankauer", "ok": False, "caduca": False}
        ],
        "Bosses Ambu": [
            {"nom": "Ambu Adult complet", "ok": False, "caduca": False},
            {"nom": "Ambu Pediàtric complet", "ok": False, "caduca": False}
        ],
        "Calaixeres i Prestatges Paret": [
            {"nom": "Calaix 1, 2 i 3 (Gasses, Tensiómetre, Guedels)", "ok": False, "caduca": False},
            {"nom": "1r Prestatge (Orinal Femení, SIPE, etc.)", "ok": False, "caduca": False},
            {"nom": "2n Prestatge (Orinal Masculí, Mantes, Llencols)", "ok": False, "caduca": False},
            {"nom": "3r Prestatge (Matalàs buit, Bosses parts/cremats)", "ok": False, "caduca": True, "data": datetime.date(2028, 9, 12)}
        ],
        "Porta Lateral": [
            {"nom": "Matalàs pediàtric", "ok": False, "caduca": False},
            {"nom": "Fernokit", "ok": False, "caduca": False},
            {"nom": "Fèrules de Kramer", "ok": False, "caduca": False}
        ]
    }

# --- CÀLCULS ESTADÍSTICS ---
total_elements = sum(len(llista) for llista in st.session_state.inventari.values())
elements_revisats = sum(sum(1 for item in llista if item["ok"]) for llista in st.session_state.inventari.values())
percentatge = int((elements_revisats / total_elements) * 100) if total_elements > 0 else 0
avui = datetime.date.today()

# --- PANEL CONTROL ---
st.write("---")
st.subheader("📊 Estat de la Revisió Actual")
col1, col2 = st.columns(2)
with col1:
    st.metric(label="Revisats", value=f"{elements_revisats} / {total_elements}")
with col2:
    st.progress(percentatge / 100)
    st.caption(f"Revisió al **{percentatge}%** completada.")

st.write("---")

# --- LLISTES INTERACTIVES ---
for categoria, llista in st.session_state.inventari.items():
    seccio_ok = all(item["ok"] for item in llista)
    titol = f"✅ {categoria}" if seccio_ok else f"📦 {categoria}"
    
    with st.expander(titol, expanded=not seccio_ok):
        for i, item in enumerate(llista):
            col_check, col_date = st.columns()
            
            with col_check:
                item["ok"] = st.checkbox(item["nom"], value=item["ok"], key=f"chk_{categoria}_{i}")
            
            with col_date:
                if item["caduca"]:
                    nova_data = st.date_input("Caducitat", value=item["data"], key=f"date_{categoria}_{i}", label_visibility="collapsed")
                    item["data"] = nova_data
                    
                    dies_restants = (nova_data - avui).days
                    if dies_restants < 0:
                        st.caption("🔴 **CADUCAT**")
                    elif dies_restants < 90:
                        st.caption("🟡 **< 3 mesos**")
                    else:
                        st.caption("🟢 OK")
                else:
                    st.caption("🔹 Permanent")

# --- GENERACIÓ DE L'INFORME FINAL ---
st.write("---")
st.subheader("📤 Finalitzar i Enviar Revisió")

data_actual = datetime.datetime.now().strftime("%d/%m/%Y %H:%M")
auditor_nom = auditor_seleccionat if auditor_seleccionat != "Triar auditor/a..." else "No seleccionat"
conductor_nom = conductor_vehicle if conductor_vehicle else "No especificat"
nom_vehicle = indicatiu_vehicle if indicatiu_vehicle else "Sense_Nom"
matricula_vehicle = detalls_vehicle if detalls_vehicle else "No especificada"

informe_text = f"=========================================\n"
informe_text += f"INFORME DE REVISIÓ DE MATERIAL\n"
informe_text += f"=========================================\n"
informe_text += f"VEHICLE / INDICATIU: {nom_vehicle}\n"
informe_text += f"MATRÍCULA / CODI: {matricula_vehicle}\n"
informe_text += f"DATA DE CONTROL: {data_actual}\n"
informe_text += f"AUDITOR/A: {auditor_nom}\n"
informe_text += f"CONDUCTOR/A: {conductor_nom}\n"
informe_text += f"PERCENTATGE VERIFICACIÓ: {percentatge}%\n"
informe_text += f"-----------------------------------------\n\n"

elements_pendents = []
elements_caducats = []

for cat, llista in st.session_state.inventari.items():
    for item in llista:
        if not item["ok"]:
            elements_pendents.append(f"- [{cat}] {item['nom']}")
        if item["caduca"] and (item["data"] - avui).days < 0:
            elements_caducats.append(f"- [{cat}] {item['nom']} (Caducat el {item['data'].strftime('%d/%m/%Y')})")

if elements_caducats:
    informe_text += "🚨 MATERIAL CADUCAT:\n" + "\n".join(elements_caducats) + "\n\n"
else:
    informe_text += "🚨 MATERIAL CADUCAT:\nCap element caducat.\n\n"

if elements_pendents:
    informe_text += "⚠️ MATERIAL PENDENT DE VERIFICAR O FALTANT:\n" + "\n".join(elements_pendents) + "\n"
else:
    informe_text += "⚠️ MATERIAL PENDENT DE VERIFICAR:\nTot el material revisat i correcte! ✅\n"

nom_arxiu_net = nom_vehicle.replace(" ", "_")
data_arxiu = datetime.date.today().strftime('%Y%m%d')

col_btn1, col_btn2 = st.columns(2)

with col_btn1:
