#pragma once

#include "esphome/components/button/button.h"
#include "../ml307r.h"

namespace esphome {
namespace ml307r {

class RebootButton : public button::Button, public Parented<ML307RComponent> {
public:
  RebootButton(uint8_t status): status_(status) {}

protected:
  uint8_t status_{0};

  void press_action() override;
};

}  // namespace ml307r
}  // namespace esphome
