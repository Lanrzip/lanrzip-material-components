# AUTO GENERATED FILE - DO NOT EDIT

#' @export
''MuiTextField <- function(id=NULL, FormHelperTextProps=NULL, InputLabelProps=NULL, InputProps=NULL, SelectProps=NULL, autoComplete=NULL, autoFocus=NULL, classes=NULL, color=NULL, defaultValue=NULL, disabled=NULL, error=NULL, fullWidth=NULL, helperText=NULL, inputProps=NULL, inputRef=NULL, label=NULL, margin=NULL, maxRows=NULL, minRows=NULL, multiline=NULL, name=NULL, onChange=NULL, placeholder=NULL, required=NULL, rows=NULL, select=NULL, size=NULL, sx=NULL, type=NULL, value=NULL, variant=NULL) {
    
    props <- list(id=id, FormHelperTextProps=FormHelperTextProps, InputLabelProps=InputLabelProps, InputProps=InputProps, SelectProps=SelectProps, autoComplete=autoComplete, autoFocus=autoFocus, classes=classes, color=color, defaultValue=defaultValue, disabled=disabled, error=error, fullWidth=fullWidth, helperText=helperText, inputProps=inputProps, inputRef=inputRef, label=label, margin=margin, maxRows=maxRows, minRows=minRows, multiline=multiline, name=name, onChange=onChange, placeholder=placeholder, required=required, rows=rows, select=select, size=size, sx=sx, type=type, value=value, variant=variant)
    if (length(props) > 0) {
        props <- props[!vapply(props, is.null, logical(1))]
    }
    component <- list(
        props = props,
        type = 'MuiTextField',
        namespace = 'lanrzip_material_components',
        propNames = c('id', 'FormHelperTextProps', 'InputLabelProps', 'InputProps', 'SelectProps', 'autoComplete', 'autoFocus', 'classes', 'color', 'defaultValue', 'disabled', 'error', 'fullWidth', 'helperText', 'inputProps', 'inputRef', 'label', 'margin', 'maxRows', 'minRows', 'multiline', 'name', 'onChange', 'placeholder', 'required', 'rows', 'select', 'size', 'sx', 'type', 'value', 'variant'),
        package = 'lanrzipMaterialComponents'
        )

    structure(component, class = c('dash_component', 'list'))
}
