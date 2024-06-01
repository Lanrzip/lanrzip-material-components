# AUTO GENERATED FILE - DO NOT EDIT

#' @export
''MuiButton <- function(children=NULL, id=NULL, classes=NULL, color=NULL, component=NULL, debounceWait=NULL, disableElevation=NULL, disableFocusRipple=NULL, disableRipple=NULL, disabled=NULL, endIcon=NULL, fullWidth=NULL, href=NULL, key=NULL, nClicks=NULL, size=NULL, startIcon=NULL, variant=NULL) {
    
    props <- list(children=children, id=id, classes=classes, color=color, component=component, debounceWait=debounceWait, disableElevation=disableElevation, disableFocusRipple=disableFocusRipple, disableRipple=disableRipple, disabled=disabled, endIcon=endIcon, fullWidth=fullWidth, href=href, key=key, nClicks=nClicks, size=size, startIcon=startIcon, variant=variant)
    if (length(props) > 0) {
        props <- props[!vapply(props, is.null, logical(1))]
    }
    component <- list(
        props = props,
        type = 'MuiButton',
        namespace = 'lanrzip_material_components',
        propNames = c('children', 'id', 'classes', 'color', 'component', 'debounceWait', 'disableElevation', 'disableFocusRipple', 'disableRipple', 'disabled', 'endIcon', 'fullWidth', 'href', 'key', 'nClicks', 'size', 'startIcon', 'variant'),
        package = 'lanrzipMaterialComponents'
        )

    structure(component, class = c('dash_component', 'list'))
}
