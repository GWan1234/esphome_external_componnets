#pragma once

#include "esphome/components/button/button.h"
#include "../ld2460.h"

namespace esphome {
namespace ld2460 {

class RestartButton : public button::Button, public Parented<LD2460Component> {
 public:
  RestartButton() = default;

 protected:
  void press_action() override;
};

}  // namespace ld2460
}  // namespace esphome
