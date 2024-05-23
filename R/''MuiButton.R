# AUTO GENERATED FILE - DO NOT EDIT

#' @export
''MuiButton <- function(children=NULL, id=NULL, nClicks=NULL, variant=NULL) {
    
    props <- list(children=children, id=id, nClicks=nClicks, variant=variant)
    if (length(props) > 0) {
        props <- props[!vapply(props, is.null, logical(1))]
    }
    component <- list(
        props = props,
        type = 'MuiButton',
        namespace = 'lanrzip_material_components',
        propNames = c('children', 'id', 'nClicks', 'variant'),
        package = 'lanrzipMaterialComponents'
        )

    structure(component, class = c('dash_component', 'list'))
}
