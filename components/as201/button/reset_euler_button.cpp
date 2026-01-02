#include "reset_euler_button.h"

namespace esphome {
namespace as201 {

void ResetEulerButton::press_action() { this->parent_->reset_euler_angle(); }

}  // namespace as201
}  // namespace esphome
