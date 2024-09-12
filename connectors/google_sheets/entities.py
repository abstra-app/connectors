from typing import Literal, List, Dict
from dataclasses import dataclass

RecalculationInterval = Literal["ON_CHANGE", "MINUTE", "HOUR"]
NumberFormatType = Literal[
    "NUMBER_FORMAT_TYPE_UNSPECIFIED",
    "TEXT",
    "NUMBER",
    "PERCENT",
    "CURRENCY",
    "DATE",
    "TIME",
    "DATE_TIME",
    "SCIENTIFIC",
]
ThemeColorType = Literal[
    "THEME_COLOR_TYPE_UNSPECIFIED",
    "TEXT",
    "BACKGROUND",
    "ACCENT1",
    "ACCENT2",
    "ACCENT3",
    "ACCENT4",
    "ACCENT5",
    "ACCENT6",
    "LINK",
]
HorizontalAlign = Literal["HORIZONTAL_ALIGN_UNSPECIFIED", "LEFT", "CENTER", "RIGHT"]
VerticalAlign = Literal["VERTICAL_ALIGN_UNSPECIFIED", "TOP", "MIDDLE", "BOTTOM"]
Style = Literal[
    "STYLE_UNSPECIFIED",
    "DOTTED",
    "DASHED",
    "SOLID",
    "SOLID_MEDIUM",
    "SOLID_THICK",
    "DOUBLE",
    "NONE",
]
WrapStrategy = Literal[
    "WRAP_STRATEGY_UNSPECIFIED", "OVERFLOW_CELL", "LEGACY_WRAP", "CLIP", "WRAP"
]
TextDirection = Literal["TEXT_DIRECTION_UNSPECIFIED", "LEFT_TO_RIGHT", "RIGHT_TO_LEFT"]
HyperlinkDisplayType = Literal[
    "HYPERLINK_DISPLAY_TYPE_UNSPECIFIED", "LINKED", "PLAIN_TEXT"
]
SheetType = Literal["SHEET_TYPE_UNSPECIFIED", "GRID", "OBJECT", "DATA_SOURCE"]
DataExecutionState = Literal[
    "DATA_EXECUTION_STATE_UNSPECIFIED",
    "NOT_STARTED",
    "RUNNING",
    "CANCELLING",
    "SUCCEEDED",
    "FAILED",
]
DataExecutionErrorCode = Literal[
    "DATA_EXECUTION_ERROR_CODE_UNSPECIFIED",
    "TIMED_OUT",
    "TOO_MANY_ROWS",
    "TOO_MANY_COLUMNS",
    "TOO_MANY_CELLS",
    "ENGINE",
    "PARAMETER_INVALID",
    "UNSUPPORTED_DATA_TYPE",
    "DUPLICATE_COLUMN_NAMES",
    "INTERRUPTED",
    "CONCURRENT_QUERY",
    "OTHER",
    "TOO_MANY_CHARS_PER_CELL",
    "DATA_NOT_FOUND",
    "PERMISSION_DENIED",
    "MISSING_COLUMN_ALIAS",
    "OBJECT_NOT_FOUND",
    "OBJECT_IN_ERROR_STATE",
    "OBJECT_SPEC_INVALID",
    "DATA_EXECUTION_CANCELLED",
]
ErrorType = Literal[
    "ERROR_TYPE_UNSPECIFIED",
    "ERROR",
    "NULL_VALUE",
    "DIVIDE_BY_ZERO",
    "VALUE",
    "REF",
    "NAME",
    "NUM",
    "N_A",
    "LOADING",
]
RelativeDate = Literal[
    "RELATIVE_DATE_UNSPECIFIED",
    "PAST_YEAR",
    "PAST_MONTH",
    "PAST_WEEK",
    "YESTERDAY",
    "TODAY",
    "TOMORROW",
]
ConditionType = Literal[
    "CONDITION_TYPE_UNSPECIFIED",
    "NUMBER_GREATER",
    "NUMBER_GREATER_THAN_EQ",
    "NUMBER_LESS",
    "NUMBER_LESS_THAN_EQ",
    "NUMBER_EQ",
    "NUMBER_NOT_EQ",
    "NUMBER_BETWEEN",
    "NUMBER_NOT_BETWEEN",
    "TEXT_CONTAINS",
    "TEXT_NOT_CONTAINS",
    "TEXT_STARTS_WITH",
    "TEXT_ENDS_WITH",
    "TEXT_EQ",
    "TEXT_IS_EMAIL",
    "TEXT_IS_URL",
    "DATE_EQ",
    "DATE_BEFORE",
    "DATE_AFTER",
    "DATE_ON_OR_BEFORE",
    "DATE_ON_OR_AFTER",
    "DATE_BETWEEN",
    "DATE_NOT_BETWEEN",
    "DATE_IS_VALID",
    "ONE_OF_RANGE",
    "ONE_OF_LIST",
    "BLANK",
    "NOT_BLANK",
    "CUSTOM_FORMULA" "BOOLEAN" "TEXT_NOT_EQ" "DATE_NOT_EQ",
    "FILTER_EXPRESSION",
]
SortOrder = Literal["SORT_ORDER_UNSPECIFIED", "ASCENDING", "DESCENDING"]
DateTimeRuleType = Literal[
    "DATE_TIME_RULE_TYPE_UNSPECIFIED",
    "SECOND",
    "MINUTE",
    "HOUR",
    "HOUR_MINUTE",
    "HOUR_MINUTE_AMPM",
    "DAY_OF_WEEK",
    "DAY_OF_YEAR",
    "DAY_OF_MONTH",
    "MONTH",
    "QUARTER",
    "YEAR",
    "YEAR_MONTH",
    "YEAR_QUARTER",
    "YEAR_MONTH_DAY",
]
PivotValueSummarizeFunction = Literal[
    "PIVOT_VALUE_SUMMARIZE_FUNCTION_UNSPECIFIED",
    "SUM",
    "COUNTA",
    "COUNT",
    "COUNTUNIQUE",
    "AVERAGE",
    "MAX",
    "MIN",
    "MEDIAN",
    "PRODUCT",
    "STDEV",
    "STDEVP",
    "VAR",
    "VARP",
    "CUSTOM" "NONE",
]
PivotValueCalculatedDisplayType = Literal[
    "PIVOT_VALUE_CALCULATED_DISPLAY_TYPE_UNSPECIFIED",
    "PERCENT_OF_ROW_TOTAL",
    "PERCENT_OF_COLUMN_TOTAL",
    "PERCENT_OF_GRAND_TOTAL",
]
PivotValueLayout = Literal["HORIZONTAL", "VERTICAL"]
DataSourceTableColumnSelectionType = Literal[
    "DATA_SOURCE_TABLE_COLUMN_SELECTION_TYPE_UNSPECIFIED", "SELECTED", "SYNC_ALL"
]
DeveloperMetadataVisibility = Literal[
    "DEVELOPER_METADATA_VISIBILITY_UNSPECIFIED", "DOCUMENT", "PROJECT"
]
DeveloperMetadataLocationType = Literal[
    "DEVELOPER_METADATA_LOCATION_TYPE_UNSPECIFIED",
    "ROW",
    "COLUMN",
    "SHEET",
    "SPREADSHEET",
]
Dimension = Literal["DIMENSION_UNSPECIFIED", "ROWS", "COLUMNS"]


class TextRotation:
    angle: int
    vertical: bool


class Color:
    red: float
    green: float
    blue: float
    alpha: float


class ColorStyle:
    rgb_color: Color
    theme_color: ThemeColorType


class Border:
    style: Style
    width: int
    color: Color
    color_style: ColorStyle


class Borders:
    top: bool
    bottom: bool
    left: bool
    right: bool


class NumberFormat:
    type: NumberFormatType
    pattern: str


class Padding:
    top: int
    bottom: int
    left: int
    right: int


class Link:
    uri: str


class TextFormat:
    foreground_color: Color
    foreground_color_style: ColorStyle
    font_family: str
    font_size: int
    bold: bool
    italic: bool
    strikethrough: bool
    underline: bool
    link: Link


class CellFormat:
    number_format: NumberFormat
    background_color: Color
    background_color_style: ColorStyle
    borders: Borders
    padding: Padding
    horizontal_alignment: HorizontalAlign
    vertical_alignment: VerticalAlign
    wrap_strategy: WrapStrategy
    text_direction: TextDirection
    text_format: TextFormat
    hyperlink_display_type: HyperlinkDisplayType
    text_rotation: TextRotation


class ThemeColorPair:
    color_type: ThemeColorType
    color: ColorStyle


class SpreadsheetTheme:
    primary_font_family: str
    theme_colors: List[ThemeColorPair]


@dataclass
class SpreadsheetProperties:
    title: str
    locale: str
    auto_recalc: RecalculationInterval
    timeZone: str
    default_format: CellFormat
    spreadsheet_theme: SpreadsheetTheme
    import_functions_external_url_access_allowed: bool


@dataclass
class Spreadsheet:
    id: str
    properties: SpreadsheetProperties


@dataclass
class GridProperties:
    row_count: int
    column_count: int
    frozen_row_count: int
    frozen_column_count: int
    hide_gridlines: bool
    row_group_control_after: bool
    column_group_control_after: bool


@dataclass
class DataSourceColumnReference:
    name: str


@dataclass
class DataSourceColumn:
    reference: DataSourceColumnReference
    formula: str


@dataclass
class DataExecutionStatus:
    state: DataExecutionState
    error_code: DataExecutionErrorCode
    error_message: str
    last_refresh_time: str


@dataclass
class DataSourceSheetProperties:
    data_source_id: str
    columns: List[DataSourceColumn]
    data_execution_status: DataExecutionStatus


@dataclass
class SheetProperties:
    sheet_id: str
    title: str
    index: int
    sheet_type: SheetType
    grid_properties: GridProperties
    hidden: bool
    tab_color: Color
    tab_color_style: ColorStyle
    right_to_left: bool
    data_source_sheet_properties: DataSourceSheetProperties


@dataclass
class ErrorValue:
    """
    An error in a cell.
    """

    type: ErrorType
    message: str


@dataclass
class ExtendedValue:
    """
    The kinds of value that a cell in a spreadsheet can have.
    """

    number_value: float
    string_value: str
    bool_value: bool
    formula_value: str
    error_value: ErrorValue


@dataclass
class TextFormatRun:
    """
    A run of a text format. The format of this run continues until the start index of the next run. When updating, all fields must be set.
    """

    start_index: int
    format: TextFormat


@dataclass
class ConditionValue:
    """
    The value of the condition.
    """

    relative_date: RelativeDate
    user_entered_value: str


@dataclass
class BooleanCondition:
    """
    A condition that can evaluate to true or false. BooleanConditions are used by conditional formatting, data validation, and the criteria in filters.
    """

    type: ConditionType
    values: List[ConditionValue]


@dataclass
class DataValidationRule:
    """
    A data validation rule.
    """

    condition: BooleanCondition
    input_message: str
    strict: bool
    show_custom_ui: bool


@dataclass
class GridRange:
    """
    A range on a sheet. All indexes are zero-based. Indexes are half open, i.e. the start index is inclusive and the end index is exclusive -- [startIndex, endIndex). Missing indexes indicate the range is unbounded on that side.
    """

    sheet_id: int
    start_row_index: int
    end_row_index: int
    start_column_index: int
    end_column_index: int


@dataclass
class PivotGroupValueMetadata:
    """
    Metadata about a value in a pivot grouping.
    """

    value: ExtendedValue
    collapsed: bool


@dataclass
class PivotGroupSortValueBucket:
    """
    Information about which values in a pivot group should be used for sorting.
    """

    values_index: int
    buckets: List[ExtendedValue]


@dataclass
class ManualRuleGroup:
    """
    A group name and a list of items from the source data that should be placed in the group with this name.
    """

    group_name: ExtendedValue
    items: List[ExtendedValue]


@dataclass
class ManualRule:
    """
    Allows you to organize the date-time values in a source data column into buckets based on selected parts of their date or time values. For example, consider a pivot table showing sales transactions by date: +----------+--------+ | Date | Sales | +----------+--------+ | 1/1/2017 | $100 | | 2/1/2017 | $123 | | 3/2/2017 | $145 | | 5/5/2017 | $178 | +----------+--------+ If you use a manual rule to group by day, the table will be organized into buckets by day, resulting in the following pivot table. +-------------+--------+ | Grouped Date | Sales | +-------------+--------+ | 1/1/2017 | $100 | | 2/1/2017 | $123 | | 3/2/2017 | $145 | | 5/5/2017 | $178 | +-------------+--------+
    """

    groups: ManualRuleGroup


@dataclass
class HistogramRule:
    """
    Allows you to organize the numeric values in a source data column into buckets of constant size. All values from HistogramRule.start to HistogramRule.end are placed into groups of size HistogramRule.interval. In addition, all values below HistogramRule.start are placed in one group, and all values above HistogramRule.end are placed in another. Only HistogramRule.interval is required, though if HistogramRule.start and HistogramRule.end are both provided, HistogramRule.start must be less than HistogramRule.end. For example, a pivot table showing average purchase amount by age that has 50+ in a bucket will have a histogram rule like the following: +-----+-----+ | Age | Amt | +-----+-----+ | 16 | $5 | | 20 | $7 | | 30 | $15 | | 50 | $100 | | 51 | $200 | +-----+-----+ HistogramRule.start = 10 HistogramRule.interval = 10 HistogramRule.end = 50 will be transformed to: +-------------+-----+ | Grouped Age | Amt | +-------------+-----+ | <10 | $5 | | 10-20 | $7 | | 20-30 | $15 | | 30-40 | $0 | | 40-50 | $150 | | 50+ | $300 | +-------------+-----+
    """

    interval: float
    start: float
    end: float


@dataclass
class DateTimeRule:
    """
    Allows you to organize the date-time values in a source data column into buckets by a given unit of time. For example, a pivot table that groups people by birthdate year could use a DateTimeRule with DateTimeRuleType.YEAR. Values will be placed in groups by based on the value of their date-time values, from the years 1960-1969, 1970-1979, 1980-1989, 1990-1999, and so on. The pivot table will also contain blank rows for people who do not have birthdates. Similar rules could be created for day of week, month, day, and so on. The DateTimeRule type requires that the column of the source data be in date-time format. For example, if the data were to represent birthdates, the source data should be formatted as m/d/yyyy.
    """

    type: DateTimeRuleType


@dataclass
class PivotGroupRule:
    """
    An optional setting on a PivotGroup that defines buckets for the values in the source data column rather than breaking out each individual value. Only one PivotGroup with a group rule may be added for each column in the source data, though on any given column you may add both a PivotGroup that has a rule and a PivotGroup that does not.
    """

    manual_rule: ManualRule
    histogram_rule: HistogramRule
    date_time_rule: DateTimeRule


@dataclass
class PivotGroupLimit:
    """
    The count limit on rows or columns in the pivot group.
    """

    count_limit: int
    apply_order: int


@dataclass
class PivotGroup:
    """
    A single grouping (either row or column) in a pivot table.
    """

    show_totals: bool
    value_metadata: PivotGroupValueMetadata
    sort_order: SortOrder
    value_bucket: PivotGroupSortValueBucket
    repeat_headings: bool
    label: str
    group_rule: PivotGroupRule
    group_limit: PivotGroupLimit
    sort_column_offset: int
    data_source_column_reference: DataSourceColumnReference


@dataclass
class PivotFilterCriteria:
    """
    Criteria for showing/hiding rows in a pivot table.
    """

    visible_values: List[str]
    condition: BooleanCondition
    visible_by_default: bool


@dataclass
class PivotFilterSpec:
    """
    The pivot table filter criteria associated with a specific source column offset.
    """

    filter_criteria: PivotFilterCriteria
    column_offset_index: int
    data_source_column_reference: DataSourceColumnReference


@dataclass
class PivotValue:
    """
    The definition of how a value in a pivot table should be calculated.
    """

    summarize_function: PivotValueSummarizeFunction
    name: str
    calculated_display_type: PivotValueCalculatedDisplayType
    source_column_offset: int
    formula: str
    data_source_column_reference: DataSourceColumnReference


@dataclass
class PivotTable:
    """
    A pivot table.
    """

    rows: List[PivotGroup]
    columns: List[PivotGroup]
    criteria: Dict[str, PivotFilterCriteria]
    filter_specs: PivotFilterSpec
    values: List[PivotValue]
    value_layout: PivotValueLayout
    data_execution_status: DataExecutionStatus
    source: GridRange
    data_source_id: str


@dataclass
class FilterCriteria:
    """
    Criteria for showing/hiding rows in a filter or filter view.
    """

    hidden_values: List[str]
    condition: BooleanCondition
    visible_background_color: Color
    visible_background_color_style: ColorStyle
    visible_foreground_color: Color
    visible_foreground_color_style: ColorStyle


@dataclass
class FilterSpec:
    """
    The filter criteria associated with a specific column.
    """

    filter_criteria: FilterCriteria
    column_index: int
    data_source_column_reference: DataSourceColumnReference


@dataclass
class SortSpec:
    """
    A sort order associated with a specific column or row.
    """

    sort_order: SortOrder
    foreground_color: Color
    foreground_color_style: ColorStyle
    background_color: Color
    background_color_style: ColorStyle
    dimension_index: int
    data_source_column_reference: DataSourceColumnReference


@dataclass
class DataSourceTable:
    """
    A data source table, which allows the user to import a static table of data from the DataSource into Sheets. This is also known as "Extract" in the Sheets editor.
    """

    data_source_id: str
    data_selection_type: DataSourceTableColumnSelectionType
    columns: List[DataSourceColumnReference]
    filter_specs: FilterSpec
    sort_specs: List[SortSpec]
    row_limit: int
    data_execution_status: DataExecutionStatus


@dataclass
class DataSourceFormula:
    """
    A data source formula.
    """

    data_source_id: str
    data_execution_status: DataExecutionStatus


@dataclass
class CellData:
    """
    Data about a specific cell.
    """

    user_entered_value: ExtendedValue
    effective_value: ExtendedValue
    formatted_value: str
    user_entered_format: CellFormat
    effective_format: CellFormat
    hyperlink: str
    note: str
    text_format_runs: List[TextFormatRun]
    data_validation: DataValidationRule
    pivot_table: PivotTable
    data_source_table: DataSourceTable
    data_source_formula: DataSourceFormula


@dataclass
class RowData:
    values: List[CellData]


@dataclass
class DimensionRange:
    """
    A range along a single dimension on a sheet. All indexes are zero-based. Indexes are half open: the start index is inclusive and the end index is exclusive. Missing indexes indicate the range is unbounded on that side.
    """

    sheet_id: int
    dimension: Dimension
    start_index: int
    end_index: int


@dataclass
class DeveloperMetadataLocation:
    """
    A location where metadata may be associated in a spreadsheet.
    """

    location_type: DeveloperMetadataLocationType
    spreadsheet: bool
    sheet_id: int
    dimension_range: DimensionRange


@dataclass
class DeveloperMetadata:
    """
    Developer metadata associated with a location or object in a spreadsheet. Developer metadata may be used to associate arbitrary data with various parts of a spreadsheet and will remain associated at those locations as they move around and the spreadsheet is edited. For example, if developer metadata is associated with row 5 and another row is then subsequently inserted above row 5, that original metadata will still be associated with the row it was first associated with (what is now row 6). If the associated object is deleted its metadata is deleted too.
    """

    metadata_id: int
    metadata_key: str
    metadata_value: str
    location: DeveloperMetadataLocation
    visibility: DeveloperMetadataVisibility


@dataclass
class DimensionProperties:
    """
    Properties about a dimension.
    """

    hidden_by_filter: bool
    hidden_by_user: bool
    pixel_size: int
    developer_metadata: List[DeveloperMetadata]
    data_source_column_reference: DataSourceColumnReference


@dataclass
class GridData:
    start_row: int
    start_column: int
    row_data: List[RowData]
    row_metadata: List[DimensionProperties]
    column_metadata: List[DimensionProperties]


@dataclass
class Sheet:
    properties: SheetProperties
    data: List[GridData]
    merges: List[GridRange]
