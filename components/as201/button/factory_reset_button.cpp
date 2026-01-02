#include "factory_reset_button.h"

namespace esphome {
namespace as201 {

void FactoryResetButton::press_action() { this->parent_->factory_reset(); }

}  // namespace as201
}  // namespace esphome
