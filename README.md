# ChatGPT Plugins Data

Extracted plugin IDs and metadata from ChatGPT's plugin store across 14 categories.

## 📊 Data Summary

- **Total Plugins**: 2,150
- **Categories**: 14
- **Last Updated**: July 19, 2026
- **Data Source**: ChatGPT Plugin API

### Category Breakdown

| Category | Count |
|----------|-------|
| featured | 12 |
| productivity | 340 |
| creativity | 83 |
| developer-tools | 119 |
| business-and-operations | 411 |
| data-and-analytics | 79 |
| communication | 22 |
| education-and-research | 128 |
| security | 21 |
| finance | 229 |
| healthcare | 50 |
| travel | 215 |
| entertainment | 87 |
| other | 355 |

## 📁 Files

### Master Files
- **`all_plugin_ids.txt`** - Complete list of all 2,150 plugin IDs (one per line)

### Category-Specific Files
- **`{category}_ids.txt`** - Plugin IDs for each category
- **`{category}_response.json`** - Full JSON responses with complete plugin metadata

## 🔍 Plugin ID Formats

The extracted IDs follow these patterns:
- `Plugin_*` - Standard plugins
- `plugin_asdk_app_*` - ASDK app plugins
- `plugin_connector_*` - Connector plugins
- `plugins_*` - Other plugin types

## 📖 JSON Response Structure

Each `{category}_response.json` file contains:

```json
{
  "plugins": [
    {
      "id": "Plugin_fc9843a6fb34819195d6c7802398a8a7",
      "display_name": "Plugin Name",
      "short_description": "Brief description",
      "keywords": ["keyword1", "keyword2"],
      "icon_url": "https://...",
      "status": "ENABLED"
    }
  ]
}
```

## 💡 Usage Examples

### Get all plugin IDs
```bash
cat all_plugin_ids.txt
```

### Get finance category plugins
```bash
cat finance_ids.txt
```

### Parse JSON for specific category
```bash
jq '.plugins[] | {id, display_name, short_description}' finance_response.json
```

## 📊 Statistics

- **Total Files**: 42
- **Total Size**: ~1.4 MB
- **Extraction Date**: July 19, 2026

---

*Extracted using ChatGPT Plugin API*
