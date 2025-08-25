import esphome.codegen as cg
import esphome.config_validation as cv
from esphome.const import DEVICE_CLASS_MOTION
from esphome.components import binary_sensor
from . import CONF_LD2451_ID, LD2451Component

DEPENDENCIES = ["ld2451"]

ICON_TARGET_ACCOUNT = "mdi:target-account"

CONF_HAS_TOWARDS_TARGET = "has_towards_target"

CONFIG_SCHEMA = cv.All(
    cv.Schema(
        {
            cv.GenerateID(CONF_LD2451_ID): cv.use_id(LD2451Component),
            cv.Optional(CONF_HAS_TOWARDS_TARGET): binary_sensor.binary_sensor_schema(
                device_class=DEVICE_CLASS_MOTION,
                icon=ICON_TARGET_ACCOUNT,
            )
        }
    )
)


async def to_code(config):
    ld2451_component = await cg.get_variable(config[CONF_LD2451_ID])
    if has_towards_target_config := config.get(CONF_HAS_TOWARDS_TARGET):
        sens = await binary_sensor.new_binary_sensor(has_towards_target_config)
        cg.add(ld2451_component.set_has_towards_target_binary_sensor(sens))
