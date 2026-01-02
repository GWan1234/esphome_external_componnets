#pragma once

#include "esphome/components/select/select.h"
#include "../as201.h"

namespace esphome {
namespace as201 {

class UploadRateSelect : public select::Select, public Parented<AS201Component> {
 public:
  UploadRateSelect() = default;

 protected:
  void control(const std::string &value) override;
};

}  // namespace as201
}  // namespace esphome
