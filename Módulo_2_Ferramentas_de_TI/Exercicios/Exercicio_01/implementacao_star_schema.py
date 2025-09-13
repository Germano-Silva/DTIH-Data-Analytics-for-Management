# implementacao_star_schema.py
# Script gerado para construir o star schema a partir do arquivo 'limpeza_modelagem.xlsx'.
# IDs seguem o padrão: [CÓDIGO][NNN] (3 dígitos), ex: PES001, EMP001, GEO001, DAT001, CAR001, SET001, SEMP001, TAM001, CON001
# Requisitos: pandas, numpy

import pandas as pd
import numpy as np
from pathlib import Path

def gen_ids(prefix, n):
    return [f"{prefix}{i:03d}" for i in range(1, n+1)]

def load_and_combine(excel_path: str) -> pd.DataFrame:
    xls = pd.ExcelFile(excel_path)
    sheets = xls.sheet_names
    dfs = []
    for s in sheets:
        d = pd.read_excel(excel_path, sheet_name=s)
        d.index = range(d.shape[0])
        d = d.reindex(range(max([pd.read_excel(excel_path, sheet_name=sh).shape[0] for sh in sheets])))
        dfs.append(d.reset_index(drop=True))
    combined = pd.concat(dfs, axis=1)
    return combined

def build_star_schema(df: pd.DataFrame, out_dir: str = "."):
    out = Path(out_dir)
    out.mkdir(parents=True, exist_ok=True)

    codes = {"Dim_Pessoa":"PES","Dim_Empresa":"EMP","Dim_Geografia":"GEO","Dim_Tempo":"DAT","Dim_Cargo":"CAR","Dim_Setor":"SET","Dim_Setor_Empresa":"SEMP","Dim_Tamanho_Empresa":"TAM","Fact_Contatos":"CON"}

    # Helper to find column among candidates
    def col_exists(*candidates):
        for c in candidates:
            if candidates is None: continue
            for c0 in candidates:
                if c0 in df.columns:
                    return c0
        return None

    # For robustness, use explicit known column names present in the cleaned file
    def choose(*candidates):
        for c in candidates:
            if c and c in df.columns:
                return c
        return None

    cidade_emp = choose("Cidade_empresa")
    estado_emp = choose("Estado_empresa")
    pais_emp = choose("Pais_empresa")

    cidade_usr = choose("Cidade_usuario")
    estado_usr = choose("Estado_usuario")
    pais_usr = choose("Pais_usuario")

    email_col = choose("E-mail","Email")
    status_email_col = choose("Status_Email","status_email")
    nome_col = choose("Nome")
    sobrenome_col = choose("Sobrenome")
    nome_completo_col = choose("Nome completo","Nome_Completo","Nome_completo")

    linkedin_col = choose("LinkedIn_Definitivo","LinkedIn_Username")
    rede_social_usuario_col = choose("Rede_Social_usuario","Rede_Social")

    nome_emp_col = choose("Nome_Empresa","Nome_empresa")
    url_emp_col = choose("URL_Empresa")
    url_rede_emp_col = choose("URL_Redes_Sociais")
    telefone_sede_col = choose("Telefone da sede")
    codigo_pais_tel_col = choose("Codigo_Pais_Telefone")

    setor_emp_col = choose("Setor_empresa")
    categoria_setor_emp_col = choose("Categoria_Setor_empresa")

    tamanho_min_col = choose("Tamanho_Min")
    tamanho_max_col = choose("Tamanho_Max")
    tamanho_medio_col = choose("Tamanho_Medio")
    cat_tamanho_col = choose("Categoria_Tamanho_Empresa")
    classificacao_emp_col = choose("Classificacao_empresa","Classificacao_empresa")

    data_col = choose("Data_Exportacao")

    setor_usuario_col = choose("Setor_Usuario","Setor_usuario")
    granularidade_col = choose("Granularidade_Setor")
    nivel_detalhe_col = choose("Nivel_Detalhe_Setor")

    cargo_col = choose("Cargo_usuario")
    area_cargo_col = choose("Area_Cargo_usuario")
    nivel_hier_col = choose("Nivel_Hierarquico_cargo_usuario")

    # Dim_Geografia
    geo_parts = []
    if all(c in df.columns for c in [cidade_emp,estado_emp,pais_emp] if c): geo_parts.append(df[[c for c in [cidade_emp,estado_emp,pais_emp] if c is not None]].rename(columns={cidade_emp:"Cidade",estado_emp:"Estado",pais_emp:"Pais"}))
    if all(c in df.columns for c in [cidade_usr,estado_usr,pais_usr] if c): geo_parts.append(df[[c for c in [cidade_usr,estado_usr,pais_usr] if c is not None]].rename(columns={cidade_usr:"Cidade",estado_usr:"Estado",pais_usr:"Pais"}))
    if geo_parts:
        geo_df = pd.concat(geo_parts, ignore_index=True).drop_duplicates().reset_index(drop=True)
    else:
        geo_df = pd.DataFrame(columns=["Cidade","Estado","Pais"])
    geo_df["Geografia_ID"] = gen_ids(codes["Dim_Geografia"], geo_df.shape[0])
    geo_df = geo_df[["Geografia_ID","Cidade","Estado","Pais"]]
    geo_df.to_csv(out/"Dim_Geografia.csv", index=False)

    # Dim_Pessoa
    pessoa_cols = [c for c in [email_col,status_email_col,nome_col,sobrenome_col,nome_completo_col,linkedin_col,rede_social_usuario_col] if c is not None and c in df.columns]
    pessoa_df = df[pessoa_cols].copy().rename(columns={email_col:"Email",status_email_col:"Status_Email",nome_col:"Nome",sobrenome_col:"Sobrenome",nome_completo_col:"Nome_Completo",linkedin_col:"LinkedIn",rede_social_usuario_col:"Usuario_Redes_Sociais"})
    if "Nome_Completo" not in pessoa_df.columns or pessoa_df["Nome_Completo"].isna().all():
        if "Nome" in pessoa_df.columns and "Sobrenome" in pessoa_df.columns:
            pessoa_df["Nome_Completo"] = pessoa_df["Nome"].astype(str).str.strip() + " " + pessoa_df["Sobrenome"].astype(str).str.strip()
        else:
            pessoa_df["Nome_Completo"] = ""
    # map geografia per row (prefer user location)
    geo_lookup = {(r.Cidade, r.Estado, r.Pais): r.Geografia_ID for r in geo_df.itertuples()}
    pessoa_geoid = []
    for i in range(df.shape[0]):
        key = (df.loc[i,cidade_usr] if cidade_usr in df.columns and pd.notna(df.loc[i,cidade_usr]) else (df.loc[i,cidade_emp] if cidade_emp in df.columns and pd.notna(df.loc[i,cidade_emp]) else None),
               df.loc[i,estado_usr] if estado_usr in df.columns and pd.notna(df.loc[i,estado_usr]) else (df.loc[i,estado_emp] if estado_emp in df.columns and pd.notna(df.loc[i,estado_emp]) else None),
               df.loc[i,pais_usr] if pais_usr in df.columns and pd.notna(df.loc[i,pais_usr]) else (df.loc[i,pais_emp] if pais_emp in df.columns and pd.notna(df.loc[i,pais_emp]) else None))
        pessoa_geoid.append(geo_lookup.get(key,None))
    pessoa_df["Geografia_ID"] = pessoa_geoid[:pessoa_df.shape[0]]
    pessoa_df = pessoa_df.drop_duplicates(subset=["Email"]).reset_index(drop=True)
    pessoa_df["Pessoa_ID"] = gen_ids(codes["Dim_Pessoa"], pessoa_df.shape[0])
    pessoa_df = pessoa_df[[c for c in ["Pessoa_ID","Email","Status_Email","Nome","Sobrenome","Nome_Completo","LinkedIn","Usuario_Redes_Sociais","Geografia_ID"] if c in pessoa_df.columns]]
    pessoa_df.to_csv(out/"Dim_Pessoa.csv", index=False)

    # Dim_Empresa
    emp_select = [c for c in [nome_emp_col,url_emp_col,url_rede_emp_col,telefone_sede_col,codigo_pais_tel_col,tamanho_min_col,tamanho_max_col,tamanho_medio_col,cat_tamanho_col,setor_emp_col,categoria_setor_emp_col,classificacao_emp_col] if c is not None and c in df.columns]
    emp_df = df[emp_select].copy()
    rename_emp = {}
    if url_rede_emp_col: rename_emp[url_rede_emp_col]="Redes_Sociais_Empresa"
    if cat_tamanho_col: rename_emp[cat_tamanho_col]="Classificacao_Tamanho_Empresa"
    if setor_emp_col: rename_emp[setor_emp_col]="Setor_Empresa"
    emp_df = emp_df.rename(columns=rename_emp)
    emp_geoid = []
    for i in range(df.shape[0]):
        key = (df.loc[i,cidade_emp] if cidade_emp in df.columns and pd.notna(df.loc[i,cidade_emp]) else None, df.loc[i,estado_emp] if estado_emp in df.columns and pd.notna(df.loc[i,estado_emp]) else None, df.loc[i,pais_emp] if pais_emp in df.columns and pd.notna(df.loc[i,pais_emp]) else None)
        emp_geoid.append(geo_lookup.get(key,None))
    emp_df["Geografia_ID"] = emp_geoid[:emp_df.shape[0]]
    if "Nome_Empresa" in emp_df.columns:
        emp_df = emp_df.drop_duplicates(subset=["Nome_Empresa"]).reset_index(drop=True)
    else:
        emp_df = emp_df.drop_duplicates().reset_index(drop=True)
    emp_df["Empresa_ID"] = gen_ids(codes["Dim_Empresa"], emp_df.shape[0])
    emp_df.to_csv(out/"Dim_Empresa.csv", index=False)

    # Dim_Tempo
    if data_col and data_col in df.columns:
        tempo_df = df[[data_col,"Ano","Mes","Dia","Trimestre","Semana","Dia_Semana"]].drop_duplicates().reset_index(drop=True)
        tempo_df = tempo_df.rename(columns={data_col:"Data_Exportacao"})
        tempo_df["Data_Completa"] = pd.to_datetime(tempo_df["Data_Exportacao"], errors="coerce")
        tempo_df["Data_ID"] = gen_ids(codes["Dim_Tempo"], tempo_df.shape[0])
        tempo_df = tempo_df[["Data_ID","Data_Completa","Ano","Mes","Dia","Trimestre","Semana","Dia_Semana"]]
        tempo_df.to_csv(out/"Dim_Tempo.csv", index=False)

    # Dim_Cargo
    cargo_cols = [c for c in [cargo_col,area_cargo_col,nivel_hier_col] if c is not None and c in df.columns]
    if cargo_cols:
        cargo_df = df[cargo_cols].copy().rename(columns={cargo_col:"Cargo", area_cargo_col:"Cargo_Area", nivel_hier_col:"Cargo_Nivel_Hierarquico"})
        cargo_df = cargo_df.drop_duplicates().reset_index(drop=True)
        cargo_df["Cargo_ID"] = gen_ids(codes["Dim_Cargo"], cargo_df.shape[0])
        cargo_df.to_csv(out/"Dim_Cargo.csv", index=False)
    else:
        cargo_df = pd.DataFrame()

    # Dim_Setor
    setor_cols = [c for c in [setor_usuario_col,granularidade_col,nivel_detalhe_col] if c is not None and c in df.columns]
    if setor_cols:
        setor_df = df[setor_cols].copy().rename(columns={setor_usuario_col:"Setor_Usuario",granularidade_col:"Granularidade_Setor",nivel_detalhe_col:"Nivel_Detalhe_Setor"})
        setor_df = setor_df.drop_duplicates().reset_index(drop=True)
        setor_df["Setor_ID"] = gen_ids(codes["Dim_Setor"], setor_df.shape[0])
        setor_df.to_csv(out/"Dim_Setor.csv", index=False)
    else:
        setor_df = pd.DataFrame()

    # Dim_Setor_Empresa
    semp_cols = [c for c in [setor_emp_col,categoria_setor_emp_col] if c is not None and c in df.columns]
    if semp_cols:
        semp_df = df[semp_cols].copy().rename(columns={setor_emp_col:"Setor_Empresa",categoria_setor_emp_col:"Categoria_Setor_empresa"})
        semp_df = semp_df.drop_duplicates().reset_index(drop=True)
        semp_df["Setor_Empresa_ID"] = gen_ids(codes["Dim_Setor_Empresa"], semp_df.shape[0])
        semp_df.to_csv(out/"Dim_Setor_Empresa.csv", index=False)
    else:
        semp_df = pd.DataFrame()

    # Dim_Tamanho_Empresa
    tam_cols = [c for c in [tamanho_min_col,tamanho_max_col,tamanho_medio_col,cat_tamanho_col,classificacao_emp_col,"Classificacao_empresa_Ordinal"] if c is not None and c in df.columns]
    if tam_cols:
        tam_df = df[[c for c in tam_cols if c in df.columns]].copy()
        tam_df = tam_df.rename(columns={cat_tamanho_col:"Classificacao_Tamanho_Empresa", classificacao_emp_col:"Classificacao_empresa"})
        tam_df = tam_df.drop_duplicates().reset_index(drop=True)
        tam_df["Tamanho_ID"] = gen_ids(codes["Dim_Tamanho_Empresa"], tam_df.shape[0])
        tam_df.to_csv(out/"Dim_Tamanho_Empresa.csv", index=False)
    else:
        tam_df = pd.DataFrame()

    # Fact_Contatos
    fact_df = pd.DataFrame(index=df.index)
    if "Email" in pessoa_df.columns:
        email_to_pessoa = pd.Series(pessoa_df.Pessoa_ID.values, index=pessoa_df.Email.values).to_dict()
        fact_df["Pessoa_ID"] = df[email_col].map(email_to_pessoa)
    if "Nome_Empresa" in emp_df.columns:
        empresa_to_id = pd.Series(emp_df.Empresa_ID.values, index=emp_df.Nome_Empresa.values).to_dict()
        fact_df["Empresa_ID"] = df[nome_emp_col].map(empresa_to_id) if nome_emp_col in df.columns else None
    if data_col and data_col in df.columns and not tempo_df.empty:
        data_map = pd.Series(tempo_df.Data_ID.values, index=tempo_df.Data_Completa.astype(str).values).to_dict()
        fact_df["Data_ID"] = pd.to_datetime(df[data_col], errors="coerce").astype(str).map(data_map)
    if not cargo_df.empty:
        cargo_map = pd.Series(cargo_df.Cargo_ID.values, index=cargo_df.Cargo.values).to_dict()
        fact_df["Cargo_ID"] = df[cargo_col].map(cargo_map) if cargo_col in df.columns else None
    if not setor_df.empty:
        setor_map = pd.Series(setor_df.Setor_ID.values, index=setor_df.Setor_Usuario.values).to_dict()
        fact_df["Setor_ID"] = df[setor_usuario_col].map(setor_map) if setor_usuario_col in df.columns else None
    fact_df["Status_Valido"] = (df[status_email_col]=="valid").astype(int) if status_email_col in df.columns else 0
    fact_df["Tem_LinkedIn"] = df[linkedin_col].notna().astype(int) if linkedin_col in df.columns else 0
    fact_df["Contato_ID"] = gen_ids(codes["Fact_Contatos"], df.shape[0])
    fact_df = fact_df.reset_index(drop=True)[["Contato_ID","Pessoa_ID","Empresa_ID","Data_ID","Cargo_ID","Setor_ID","Status_Valido","Tem_LinkedIn"]]
    fact_df.to_csv(out/"Fact_Contatos.csv", index=False)

    print("Star schema built and CSVs saved to", out)

if __name__ == "__main__":
    excel = "limpeza_modelagem.xlsx"
    df = load_and_combine(excel)
    build_star_schema(df, out_dir=".")