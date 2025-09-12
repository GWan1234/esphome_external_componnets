#include "factory_reset_button.h"

namespace esphome {
namespace ld2460 {

void FactoryResetButton::press_action() { this->parent_->factory_reset(); }

}  // namespace ld2460
}  // namespace esphome
