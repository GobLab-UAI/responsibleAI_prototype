MODEL_CARD_HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<title>Model Card</title>
<style>
    body {{
      font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
      color: #333;
      margin: 0;
      padding: 0;
      background-color: #eaeaea;
    }}
    .container {{
      max-width: 800px;
      margin: auto;
      background-color: #fff;
      padding: 20px;
      box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
    }}
    .column-container {{
      column-count: 2;
      column-gap: 40px;
    }}
    h1 {{
      color: #20c997;
      font-size: 22px;
      text-align: center;
      margin-bottom: 24px;
      column-span: all; /* Hace que el título se extienda a través de todas las columnas */
    }}
    h2, p, ul, li {{
      font-size: 14px;
      color: #333;
      line-height: 1.6;
    }}
    .footer {{
    font-size: 12px;
    text-align: center;
    margin-top: 20px;
    color: #666;
   }}
    @media screen and (max-width: 768px) {{
      .column-container {{
        column-count: 1; /* Cambia a una sola columna para pantallas más pequeñas */
      }}
    }}
  </style>
</head>
<body>
<div class="container">
  <h1>{nombre_modelo}</h1>
  <div class="column-container">
    <div class="column">
      <h2>Detalles del Modelo</h2>
      <ul>
        <li>Modelo desarrollado por: <strong>{desarrollador_modelo}</strong> </li>
        <li>Versión del modelo: <strong>{version_modelo}</strong></li>
        <li>Fecha de implementación: {fecha_modelo} </li>
        <li>{tipo_modelo}</li>
        {link_modelo_line}
        {cita_modelo_line}
        {licencia_modelo_line}
        {contacto_modelo_line}
      </ul>

      <h2>Visión general del modelo</h2>
      <ul>
        <li>{proposito_modelo}</li>
        {TA_porque_modelo_line}
        {TA_alcanzar_resultados_line}
        <li>Uso previsto del modelo: {UsoPrevisto_modelo}</li>
        <li>{UsosNocontext_modelo}</li>
      </ul>

      <!-- Este es el render de TA que está pendiente para agregar-->
      <!--Bloque TA-->
     <div {TA_classModelo_visible}>
        <h2>Clasificación</h2>
        <ul>
          <li>Categorías del modelo: {TA_classModelo_categorias}</li>
          {TA_classModel_metodologia_line}
          {TA_classModelo_efecto_variables_line}
          {TA_classModelo_relevancia_categoria_line}
        </ul>
      </div>

      <!--FIN BLOQUE TA-->
    
      <h2>Métricas de rendimiento</h2>
      <p>{metricas_modelo}</p>
      <ul>
        <li>Umbral de decisión: {umbralDesicion_modelo}</li>
      </ul>
      {calculo_mediciones_modelo_line}
      
      <h2>Datos de Entrenamiento</h2>
      <p>{datos_modelo}</p>
      <p>Preprocesamiento de los datos: {preprocesamiento_modelo}</p>

      <h2>Datos de Evaluación</h2>
      <p>{conjunto_datos_eval_modelo}</p>
      {eleccion_evaluacion_line}
      <p>Preprocesamiento de los datos para evaluación: {preprocesamiento_evaluacion}</p>


      <h2>Consideraciones Éticas</h2>
      <h5>El modelo {TA_modelo_categoriza} categoriza las personas</h5> 
      {TA_razones_decision_negativa_personas_line}
      
      <h5>El modelo {TA_datos_personales} usa datos personales</h5> <!--CAmbiar a checkbox-->
      {TA_razones_datos_personales_line}

      <h5>El modelo {dato_sensible} usa datos sensibles</h5>
      {dato_sensible_tipo_line}
      
      <h5>El modelo {asuntos_centrales_modelo} toma decisiones importantes para la vida</h5>
      {asuntos_centrales_tipo_line}

      {estrategias_mitigaciones_modelo_line}
      
      {riesgos_uso_modelo_line}

      {casos_uso_conocidos_line}

      {otra_consideracion_line}

      <h2>Advertencias y Recomendaciones</h2>
      {prueba_adicional_line}
      <p>{grupo_relevante} hay grupos relevantes NO representados en el conjunto de datos.</p>
      {recomendaciones_adicionales_line}

      {caracteristicas_ideales_line}

      <h2>Reclamaciones</h2>
      <p>El modelo {TA_reclamacion} tiene una vía para realizar reclamaciones.</p>
      {TA_via_reclamacion_line}
    </div>
  </div>
</div>
<div class="footer">
    <p>© {year} Herramienta de model card diseñada por GobLab. Todos los derechos reservados.</p>
    <p>Elaborado en {elaboration_date}.</p>
</div>
</body>
</html>

"""
