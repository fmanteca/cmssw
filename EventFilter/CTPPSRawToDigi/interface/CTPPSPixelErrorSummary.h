#ifndef EventFilter_CTPPSRawToDigi_CTPPSPixelErrorSummary
#define EventFilter_CTPPSRawToDigi_CTPPSPixelErrorSummary

#include <string>
#include <map>

class CTPPSPixelErrorSummary {
public:
  CTPPSPixelErrorSummary(const std::string& category, const std::string& name, bool debug = false)
      : m_debug(debug), m_category(category), m_name(name) {}

  void add(const std::string& message, const std::string& details = "");
  void printSummary() const;

private:
  bool m_debug;
  std::string m_category;
  std::string m_name;
  std::map<std::string, std::size_t> m_errors;
};
#endif
