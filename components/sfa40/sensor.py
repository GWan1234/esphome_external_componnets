import esphome.codegen as cg
import esphome.config_validation as cv
from esphome.components import i2c, sensirion_common, sensor
from esphome.const import (
    CONF_ID,
    CONF_TEMPERATURE,
    STATE_CLASS_MEASUREMENT,
    UNIT_CELSIUS, DEVICE_CLASS_TEMPERATURE,
    CONF_FORMALDEHYDE,
    UNIT_PARTS_PER_BILLION, ICON_RADIATOR, DEVICE_CLASS_GAS, CONF_HUMIDITY, UNIT_PERCENT, ICON_WATER_PERCENT,
    DEVICE_CLASS_HUMIDITY, ICON_THERMOMETER,
)

CODEOWNERS = ["@synodriver"]
DEPENDENCIES = ["i2c"]
AUTO_LOAD = ["sensirion_common"]

sfa40 = cg.esphome_ns.namespace("sfa40")
SFA40Component = sfa40.class_("SFA40Component", cg.PollingComponent, sensirion_common.SensirionI2CDevice)

CONFIG_SCHEMA = cv.All(
    cv.Schema(
        {
            cv.GenerateID(): cv.declare_id(SFA40Component),
            cv.Optional(CONF_FORMALDEHYDE): sensor.sensor_schema(
                unit_of_measurement=UNIT_PARTS_PER_BILLION,
                icon=ICON_RADIATOR,
                accuracy_decimals=1,
                device_class=DEVICE_CLASS_GAS,
                state_class=STATE_CLASS_MEASUREMENT,
            ),
            cv.Optional(CONF_HUMIDITY): sensor.sensor_schema(
                unit_of_measurement=UNIT_PERCENT,
                icon=ICON_WATER_PERCENT,
                accuracy_decimals=2,
                device_class=DEVICE_CLASS_HUMIDITY,
                state_class=STATE_CLASS_MEASUREMENT,
            ),
            cv.Optional(CONF_TEMPERATURE): sensor.sensor_schema(
                unit_of_measurement=UNIT_CELSIUS,
                icon=ICON_THERMOMETER,
                accuracy_decimals=2,
                device_class=DEVICE_CLASS_TEMPERATURE,
                state_class=STATE_CLASS_MEASUREMENT,
            ),
        }
    )
    .extend(cv.polling_component_schema("60s"))
    .extend(i2c.i2c_device_schema(0x5D)),
)

FINAL_VALIDATE_SCHEMA = i2c.final_validate_device_schema("sfa40", max_frequency="100khz") # todo 100khz?


async def to_code(config):
    var = cg.new_Pvariable(config[CONF_ID])
    await cg.register_component(var, config)
    await i2c.register_i2c_device(var, config)

    if CONF_FORMALDEHYDE in config:
        sens = await sensor.new_sensor(config[CONF_FORMALDEHYDE])
        cg.add(var.set_formaldehyde_sensor(sens))
    if CONF_HUMIDITY in config:
        sens = await sensor.new_sensor(config[CONF_HUMIDITY])
        cg.add(var.set_humidity_sensor(sens))
    if CONF_TEMPERATURE in config:
        sens = await sensor.new_sensor(config[CONF_TEMPERATURE])
        cg.add(var.set_temperature_sensor(sens))
