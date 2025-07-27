-- Estructura base para WEB_REGISTRO

-- Tabla de usuarios del sistema (incluye admin, colaboradores, invitados)
CREATE TABLE IF NOT EXISTS usuarios (
    usuario_id SERIAL PRIMARY KEY,
    nombre TEXT NOT NULL,
    username TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL,
    rol TEXT NOT NULL DEFAULT 'invitado', -- admin, colaborador, invitado
    es_invitado BOOLEAN DEFAULT FALSE
);

-- Tabla de promotores 
CREATE TABLE IF NOT EXISTS promotores (
    promotor_id SERIAL PRIMARY KEY,
    nombre TEXT NOT NULL,
    apellido TEXT NOT NULL,
    domicilio TEXT,
    celular TEXT,
    seccion TEXT NOT NULL,
    municipio TEXT NOT NULL
);

-- Tabla general de afiliados (inician en el ID 1000 para futuros QR)
CREATE SEQUENCE IF NOT EXISTS afiliado_id_seq START 1000;
CREATE TABLE IF NOT EXISTS afiliados (
    afiliado_id INTEGER PRIMARY KEY DEFAULT nextval('afiliado_id_seq'),
    nombre TEXT NOT NULL,
    apellido TEXT NOT NULL,
    domicilio TEXT,
    celular TEXT,
    seccion TEXT NOT NULL,
    municipio TEXT,
    promotor_id INTEGER REFERENCES promotores(promotor_id),
    usuario_id INTEGER REFERENCES usuarios(usuario_id)
);

-- Tabla de reuniones
CREATE TABLE IF NOT EXISTS reuniones (
    reunion_id SERIAL PRIMARY KEY,
    lugar TEXT NOT NULL,
    fecha TIMESTAMP NOT NULL,
    descripcion TEXT
);

-- Asistencia de promotores a reuniones (relación N:M)
CREATE TABLE IF NOT EXISTS asistencias (
    asistencia_id SERIAL PRIMARY KEY,
    promotor_id INTEGER REFERENCES promotores(promotor_id),
    reunion_id INTEGER REFERENCES reuniones(reunion_id),
    presente BOOLEAN,
    fecha TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);


-- Historial de cambios en afiliados
CREATE TABLE IF NOT EXISTS historial_afiliados (
    historial_id SERIAL PRIMARY KEY,
    afiliado_id INTEGER REFERENCES afiliados(afiliado_id),
    operacion TEXT,
    campo_modificado TEXT,
    valor_anterior TEXT,
    valor_nuevo TEXT,
    usuario_id INTEGER REFERENCES usuarios(usuario_id),
    fecha TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);



-- Trigger y función para registrar cambios en afiliados
CREATE OR REPLACE FUNCTION registrar_cambio_afiliado()
RETURNS TRIGGER AS $$
BEGIN
    IF TG_OP = 'UPDATE' THEN
        -- Comparar celular
        IF OLD.celular IS DISTINCT FROM NEW.celular THEN
            INSERT INTO historial_afiliados (afiliado_id, operacion, campo_modificado, valor_anterior, valor_nuevo, usuario_id)
            VALUES (OLD.afiliado_id, 'UPDATE', 'celular', OLD.celular, NEW.celular, NEW.promotor_id);
        END IF;
        -- Comparar domicilio
        IF OLD.domicilio IS DISTINCT FROM NEW.domicilio THEN
            INSERT INTO historial_afiliados (afiliado_id, operacion, campo_modificado, valor_anterior, valor_nuevo, usuario_id)
            VALUES (OLD.afiliado_id, 'UPDATE', 'domicilio', OLD.domicilio, NEW.domicilio, NEW.promotor_id);
        END IF;
    END IF;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER trigger_historial_afiliados
AFTER UPDATE ON afiliados
FOR EACH ROW
EXECUTE FUNCTION registrar_cambio_afiliado();
