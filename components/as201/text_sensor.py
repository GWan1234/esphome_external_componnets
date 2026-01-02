import esphome.codegen as cg
from esphome.components import text_sensor
import esphome.config_validation as cv
from esphome.const import (
    CONF_VERSION, ENTITY_CATEGORY_DIAGNOSTIC, ICON_CHIP, CONF_TYPE, CONF_ACCURACY
)

from . import CONF_AS201_ID, AS201Component

DEPENDENCIES = ["as201"]


CONFIG_SCHEMA = cv.All(
    cv.Schema(
        {
            cv.GenerateID(CONF_AS201_ID): cv.use_id(AS201Component),
            cv.Optional(CONF_VERSION): text_sensor.text_sensor_schema(
                entity_category=ENTITY_CATEGORY_DIAGNOSTIC,
                icon=ICON_CHIP,
            ),
            cv.Optional(CONF_TYPE): text_sensor.text_sensor_schema(
                entity_category=ENTITY_CATEGORY_DIAGNOSTIC,
                icon=ICON_CHIP,
            ),
            cv.Optional(CONF_ACCURACY): text_sensor.text_sensor_schema(
                entity_category=ENTITY_CATEGORY_DIAGNOSTIC,
                icon=ICON_CHIP,
            ),
        }
    )
)


async def to_code(config):
    as201_component = await cg.get_variable(config[CONF_AS201_ID])

    if version_config := config.get(CONF_VERSION):
        sens = await text_sensor.new_text_sensor(version_config)
        cg.add(as201_component.set_version_text_sensor(sens))
    if type_config := config.get(CONF_TYPE):
        sens = await text_sensor.new_text_sensor(type_config)
        cg.add(as201_component.set_type_text_sensor(sens))
    if accuracy_config := config.get(CONF_ACCURACY):
        sens = await text_sensor.new_text_sensor(accuracy_config)
        cg.add(as201_component.set_accuracy_text_sensor(sens))