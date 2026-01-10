#include "reboot_button.h"

namespace esphome {
namespace ml307r {

void RebootButton::press_action() { this->parent_->shutdown(this->status_); }

}  // namespace ml307r
}  // namespace esphome
