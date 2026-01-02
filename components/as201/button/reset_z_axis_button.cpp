#include "reset_z_axis_button.h"

namespace esphome {
namespace as201 {

void ResetZAxisButton::press_action() { this->parent_->reset_z_axis(); }

}  // namespace as201
}  // namespace esphome
