#pragma once

#include "esphome/components/switch/switch.h"
#include "../ld2460.h"

namespace esphome {
namespace ld2460 {

class EnableUploadSwitch : public switch_::Switch, public Parented<LD2460Component> {
 public:
  EnableUploadSwitch() {
    this->turn_on();
  }

 protected:
  void write_state(bool state) override;
};

}  // namespace ld2460
}  // namespace esphome
