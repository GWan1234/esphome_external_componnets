import esphome.codegen as cg
import esphome.config_validation as cv
from esphome.components import sensor, i2c
from esphome.const import (
    CONF_ID,
    STATE_CLASS_MEASUREMENT,
    DEVICE_CLASS_PRESSURE, CONF_PRESSURE
)

CODEOWNERS = ["@synodriver"]
DEPENDENCIES = ["i2c"]

CONF_A = "a"
CONF_B = "b"
UNIT_KPASCAL = "kPa"

cps610 = cg.esphome_ns.namespace("cps610")
CPS610Component = cps610.class_("CPS610Component", cg.PollingComponent, i2c.I2CDevice)

CONFIG_SCHEMA = cv.All(
    cv.Schema(
        {
            cv.GenerateID(): cv.declare_id(CPS610Component),
            cv.Optional(CONF_A): cv.float_,
            cv.Optional(CONF_B): cv.float_,
            cv.Optional(CONF_PRESSURE): sensor.sensor_schema(
                unit_of_measurement=UNIT_KPASCAL,
                accuracy_decimals=2,
                device_class=DEVICE_CLASS_PRESSURE,
                state_class=STATE_CLASS_MEASUREMENT,
            ),
        }
    )
    .extend(cv.polling_component_schema("20s"))
    .extend(i2c.i2c_device_schema(0x7F)),
)

FINAL_VALIDATE_SCHEMA = i2c.final_validate_device_schema("cps610", max_frequency="400khz")


async def to_code(config):
    var = cg.new_Pvariable(config[CONF_ID])
    await cg.register_component(var, config)
    await i2c.register_i2c_device(var, config)

    if CONF_A in config:
        cg.add(var.set_a(config[CONF_A]))
    if CONF_B in config:
        cg.add(var.set_b(config[CONF_B]))
    if CONF_PRESSURE in config:
        sens = await sensor.new_sensor(config[CONF_PRESSURE])
        cg.add(var.set_pressure_sensor(sens))
