#pragma once

#include "esphome/components/select/select.h"
#include "../as201.h"

namespace esphome {
namespace as201 {

class BaudRateSelect : public select::Select, public Parented<AS201Component> {
 public:
  BaudRateSelect() = default;

 protected:
  void control(const std::string &value) override;
};

}  // namespace as201
}  // namespace esphome
