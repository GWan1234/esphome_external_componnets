#include "restart_button.h"

namespace esphome {
namespace as201 {

void RestartButton::press_action() { this->parent_->restart(); }

}  // namespace as201
}  // namespace esphome
