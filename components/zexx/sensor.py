from esphome import automation
import esphome.codegen as cg
import esphome.config_validation as cv
from esphome.components import sensor, uart
from esphome.const import (
    CONF_ID,
    CONF_NITROGEN_DIOXIDE,
    STATE_CLASS_MEASUREMENT,
    UNIT_PARTS_PER_BILLION,
    ICON_CHEMICAL_WEAPON,
    DEVICE_CLASS_OZONE,
    DEVICE_CLASS_AQI,
    CONF_TEMPERATURE,
    CONF_HUMIDITY, CONF_MODE,
)

CODEOWNERS = ["@synodriver"]
DEPENDENCIES = ["i2c"]
ICON_GAS_BURNER = "mdi:gas-burner"
CONF_GAS = "gas"

zexx = cg.esphome_ns.namespace("zexx")
ZEXXComponent = zexx.class_("ZEXXComponent", cg.PollingComponent, uart.UARTDevice)

ZEXX_MODE = zexx.enum("ZEXX_MODE")
ZEXX_MODE_OPTIONS = {
    "passive": ZEXX_MODE.ZEXX_MODE_PASSIVE,
    "active": ZEXX_MODE.ZEXX_MODE_ACTIVE,
}


CONFIG_SCHEMA = cv.All(
    cv.Schema(
        {
            cv.GenerateID(): cv.declare_id(ZEXXComponent),
            cv.Optional(CONF_GAS): sensor.sensor_schema(
                unit_of_measurement=UNIT_PARTS_PER_BILLION,
                accuracy_decimals=0,
                device_class=DEVICE_CLASS_OZONE,
                state_class=STATE_CLASS_MEASUREMENT,
            ),
            cv.Optional(CONF_MODE, default="passive"): cv.enum(ZEXX_MODE_OPTIONS),
        }
    )
    .extend(cv.polling_component_schema("20s"))
    .extend(uart.UART_DEVICE_SCHEMA),
)

FINAL_VALIDATE_SCHEMA = uart.final_validate_device_schema(
    "zexx",
    baud_rate=9600,
    require_tx=True,
    require_rx=True,
    parity=None,
    stop_bits=1,
)


async def to_code(config):
    var = cg.new_Pvariable(config[CONF_ID])
    await cg.register_component(var, config)
    await uart.register_uart_device(var, config)

    if CONF_GAS in config:
        sens = await sensor.new_sensor(config[CONF_GAS])
        cg.add(var.set_gas_sensor(sens))
    cg.add(var.set_mode(config[CONF_MODE]))